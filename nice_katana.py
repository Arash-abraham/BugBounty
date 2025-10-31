import os

def nice_katana(input_file=None):
    try:
        if input_file is None:
            input_file = "/dev/stdin"

        with open(input_file, "r") as f:
            for line in f:
                host = line.strip().split()[0]
                output_file = f"{host}.katana"
                command = f"echo '{line.strip()}' | katana -js-crawl -jsluice -known-files all -automatic-form-fill -silent -crawl-scope {host} -extension-filter json,js,fnt,ogg,css,jpg,jpeg,png,svg,img,gif,exe,mp4,flv,pdf,doc,ogv,webm,wmv,webp,mov,mp3,m4a,m4p,ppt,pptx,scss,tif,tiff,ttf,otf,woff,woff2,bmp,ico,eot,htc,swf,rtf,image,rf,txt,ml,ip | tee {output_file}"
                os.system(command)
    except KeyboardInterrupt:
        print('\nBy\n')
nice_katana()

#  run => echo 'domain.tld' | python3 nice_katana.py
