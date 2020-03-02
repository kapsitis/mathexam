package lv.ddgatve.discrete.ch01

object TaylorSeries {

  def factorial(n:Int):Double = {
    n match {
      case 0 => 1.0
      case n => n*factorial(n-1)
    }
  }
    
  def sin(x:Double,nTerms:Int):Double = {
    val terms = 
      for (k <- List.range(0,nTerms)) 
        yield { math.pow(-1,k)*
        math.pow(x,2*k+1)/factorial(2*k+1) } 
    terms.foldLeft(0.0)((a,b) => a+b)
  }
  
  def main(args:Array[String]): Unit = {
    val nTerms = 20
    val x = Math.PI*6 // (1080/180)*PI = 6PI 
    println(sin(x,nTerms))
  }
}