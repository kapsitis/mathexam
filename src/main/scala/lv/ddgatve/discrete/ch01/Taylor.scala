package lv.ddgatve.discrete.ch01

object Taylor {
  def sin(x:Double):Double = {
    return x*x
  }
  
  def main(args: Array[String]): Unit = {
    val x = scala.math.Pi/6
    println(sin(x))    
  }
}