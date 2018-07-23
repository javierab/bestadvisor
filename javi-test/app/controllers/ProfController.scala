package controllers

import play.api.db._
import play.api.mvc._
import javax.inject._
import java.sql.{Connection, DriverManager, ResultSet};
import java.util.Map;
import play.api.data._
import play.api.data.Forms._
import models.DescForm

@Singleton
class ProfController @Inject()(db: Database, cc: ControllerComponents) (implicit assetsFinder: AssetsFinder)
extends AbstractController(cc) with play.api.i18n.I18nSupport {
  
  
  // gets list of available professors in the DB.
  def getList = Action {
    var lst : List[String] = List()
    val conn = db.getConnection()
    
    try {
      // get list of names.
      val stmt = conn.createStatement
      val rs = stmt.executeQuery("select \"name\" from prof order by name desc;")
      
      while (rs.next()) {
        val name = rs.getString("name")
        lst = name :: lst      
      }
    } finally {
      conn.close()
    }
   
    Ok(views.html.proflist("List of professors", lst))
  } 
 
  
  // receives a description for professor matching
  // and displays the top ranked professors
  def postDescription = Action { implicit request => 
    DescForm.form.bindFromRequest.fold(
      formWithErrors => {
          BadRequest(views.html.index("bai"))
        },
        descData => {
          val desc = generateVector(descData.description)
        /* binding success, you get the actual value. */
          Ok(views.html.topiclist("Suggested Advisors for: " + descData.description, desc))
        }
      )
    }
  
  
  // generate the vector given your keywords. We assume here we get n keywords separated by "and" 
  def generateVector(desc: String) : List[(String, String)] = {
    
    val conn = db.getConnection()
    var vec = Array.fill(10)(0)

    try {

      val tstr = "select area_id-1 area from topicarea where " + {
                desc
                .split("and")
                .map(x => x.trim())
                .fold("")((x,y) 
                  => "topic like '%" +  y.toLowerCase() + 
                    (if (x.length>0) "%' or " else "%'") 
                     + x)}

      // find topics and see which areas are relevant. 
      val stmt = conn.createStatement
      val rs = stmt.executeQuery(tstr);
      
      // make the vector
      while (rs.next()) vec(rs.getInt("area"))+=1
      // get the closest profs.
      closestNeighbors(conn, vec.toList)    
      
    } finally {
      conn.close()
    }
  }

  // get the "closest neighbor" using the passed array.
  // returns the names and topics of the top 5 people.
  def closestNeighbors(conn: Connection, arr: List[Int]) : List[(String, String)] = {

    var qstr = """select al.name, al.topics, sum(abs(al.c1-al.c2)) 
                from (select name, topics, unnest(areas) c1, 
                unnest(Array[""" + arr.mkString(",") + """]) c2 
                from prof) al group by al.name, al.topics 
                order by sum(abs(al.c1-al.c2)) asc limit 5;"""
                
    var l : List[(String, String)] = List()
    val stmt = conn.createStatement
    val rs = stmt.executeQuery(qstr)

    while (rs.next()){
      l = l :+ (Pair(rs.getString("name"), rs.getString("topics")))
    }
    
    l
  }
  
}



