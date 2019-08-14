import os
import shutil
import subprocess


def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def rmDirectory(src):
    try: 
        shutil.rmtree(src)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not removed. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not removed. Error: %s' % e)


def main(): 
    rmDirectory('target')

    ## Process presentation files?
    copyDirectory('src/main/reveal.js', 'target/reveal.js')
 
    ## Process markdown stuff
    ROOT = 'src/main/markdown'
    TARGETROOT = 'target'
    subDirectories = set(next(os.walk(ROOT))[1]).difference(set(['themes','style']))
    for dd in subDirectories:
        if not os.path.exists('%s/%s' % (TARGETROOT,dd)):
            os.mkdir('%s/%s' % (TARGETROOT,dd))
        if os.path.exists('%s/%s/static' % (ROOT,dd)):
            copyDirectory('%s/%s/static' % (ROOT,dd), '%s/%s/static' % (TARGETROOT,dd))
        print('Processing "%s" with pandoc' % dd)
        md_files = os.listdir('%s/%s' % (ROOT,dd))
        for ff in md_files:
            if ff.endswith('.md'):
                newff = ff.replace('.md','.html')
                srcPath = '%s/%s/%s' % (ROOT,dd,ff)
                destPath = '%s/%s/%s' % (TARGETROOT,dd,newff)
                print('destPath = %s' % destPath)
  
                subprocess.call(['pandoc','-s','-o',destPath,
                    srcPath,
                    '--metadata', 'pagetitle="Uzdevumi"',
                    '--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
                   '--css=../style/default.css'])
    copyDirectory('src/main/markdown/style', 'target/style') 


if __name__ == '__main__':
    main()



