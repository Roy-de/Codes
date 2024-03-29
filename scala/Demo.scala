import java.io._
import implicit._

class Point(val xc: Int, val yc :Int){
   var x : Int = xc
   var y : Int = yc

   def move(dx: Int, dy :Int){
      x = x + dx
      y = x + dy
      println("Point x location: " + x)
      println("Point y location: " + y)
    }
}
class Location(override val xc: Int ,override val yc: Int, val zc :Int)extends Point(xc,yc){
   var z: Int = zc

   def move(dx: Int, dy: Int,dz: Int){
      x = x + dx
      y = y + dy
      z = z + dz
      println("Point x location: " + x)
      println("point y location: " + y)
      println("Point z location: " + z)
   }
}

object Demo{
  def main(args: Array[String]){
     val pt =  new Point(10,20)
     val loc = new Location(10,20,15)

     pt.move(10,10)
     loc.move(10,10,15)
   }
}
