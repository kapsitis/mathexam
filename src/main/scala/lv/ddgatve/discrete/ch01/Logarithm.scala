package lv.ddgatve.discrete.ch01

object Logarithm {
  
  
  def log2_recurr(k:Int, p:Int, q:Int, r:Int):Int = {
    println(s"(log2_recurr $k $p $q $r)")
    if (k == 0) {
      return p
    } 
    else {
      val k1 = k - 1
      if (r == 0) {
        return log2_recurr (k1, p+1, q+1, q)
      } else {
        val r1 = r - 1
        log2_recurr(k1, p, q+1, r1)
      }
    }
  }
  
  def main(args: Array[String]):Unit = {
    val result = log2_recurr(10,0,1,0)
    println(s"result = $result")
  }
  
}