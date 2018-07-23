package models

import play.api.data.Form
import play.api.data.Forms._

case class DescForm(description: String)

object DescForm {
  val form: Form[DescForm] = Form(
    mapping(
      "description" -> nonEmptyText
    )(DescForm.apply)(DescForm.unapply)
  )
}
