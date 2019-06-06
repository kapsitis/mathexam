package lv.ddgatve.mathexam.site

import java.io.File
import java.io.PrintWriter
import scala.io.Source
import com.github.rjeschke.txtmark.Processor

object MainSite {

  def mkSubdir(dName: String): Unit = {
    print(s"Creating $dName...\n")
    val directory = new File(dName)
    if (!directory.exists()) {
      val res = directory.mkdirs()
    }
  }

  val PREFIX = """<html>
<head>
<title>Virsraksts</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<link rel="stylesheet" type="text/css" href="style/default.css"/>
</head>
<body>"""
  
    val PREFIX2 = """<html>
<head>
<title>Virsraksts</title>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<link rel="stylesheet" type="text/css" href="../style/default.css"/>
</head>
<body>"""

  val SUFFIX = """</body>
</html>"""

  def listFiles(dir: String, ext: String): List[String] = {
    val d = new File(dir)
    val res = if (d.exists && d.isDirectory) {
      d.listFiles.filter(_.isFile).toList
    } else {
      List[File]()
    }
    return res.map(f => f.getName).filter(_.endsWith(ext))
  }

  def getPlainName(fName: String): String = {
    val res = fName.split("\\.")
    return res(0)
  }

  def main(args: Array[String]): Unit = {
    val srcDir = "src/main/markdown"
    val destDir = "target/site"
    val subDirs = List("algorithms", "all-courses", "datamgmt", "discrete", "isd", 
        "itsecurity", "LU", "RBS", "visualizations")

    for (subDir <- subDirs) {
      val files = listFiles(s"$srcDir/$subDir", ".md").map(f => getPlainName(f))

      for (ff <- files) {
        val fName = s"$srcDir/$subDir/$ff.md"
        val fileContents = Source.fromFile(fName).getLines.mkString("\n")
        val result = Processor.process(fileContents)

        val targetDir = s"$destDir/$subDir"
        mkSubdir(targetDir)
        new PrintWriter(s"$targetDir/$ff.html") {
          write((if (subDir.length()==0) PREFIX else PREFIX2) + 
              result + SUFFIX)
          close
        }
      }
    }
  }
}