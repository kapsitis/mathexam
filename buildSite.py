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

    ## Process static files
    copyDirectory('src/main/reveal.js', 'target/reveal.js')
    copyDirectory('src/main/style', 'target/style')
    ROOT = 'src/main/static'    
    subDirectories = set(next(os.walk(ROOT))[1]).difference(set(['themes']))
    for dd in subDirectories:
        copyDirectory('%s/%s' % (ROOT,dd), 'target/%s' % dd)

    ## Process markdown stuff
    ROOT = 'src/main/markdown'    
    subDirectories = set(next(os.walk(ROOT))[1]).difference(set(['themes']))
    for dd in subDirectories:
        print('Processing "%s" with pandoc' % dd)
        md_files = os.listdir('%s/%s' % (ROOT,dd))
        for ff in md_files:
            if ff.endswith('.md'):
                newff = ff.replace('.md','.html')
                srcPath = '%s/%s/%s' % (ROOT,dd,ff)
                destPath = '%s/%s/%s' % (ROOT,dd,newff)
                print('destPath = %s' % destPath)
  
                subprocess.call(['pandoc','-s','-o',destPath,
                    srcPath,
                    '--metadata', 'pagetitle="Uzdevumi"',
                    '--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
                   '--css=../style/default.css'])
        copyDirectory('%s/%s' % (ROOT,dd), 'target/%s' % dd)




if __name__ == '__main__':
    main()



