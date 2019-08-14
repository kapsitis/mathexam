import os
import shutil
import subprocess
import sys

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
    if len(sys.argv) < 2: 
        print("Specify input directory")
    else:
        dd = sys.argv[1]
        print('Processing "%s" with pandoc' % dd)
        md_files = os.listdir('%s' % dd)
        for ff in md_files:
            if ff.endswith('.md'):
                newff = ff.replace('.md','.html')
                srcPath = '%s/%s' % (dd,ff)
                destPath = '%s/%s' % (dd,newff)
                print('destPath = %s' % destPath)
  
                subprocess.call(['pandoc','-s','-o',destPath,
                    srcPath,
                    '--metadata', 'pagetitle="Uzdevumi"',
                    '--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
                   '--css=../../style/default.css'])

if __name__ == '__main__':
    main()



