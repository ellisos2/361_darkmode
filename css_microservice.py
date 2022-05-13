import time

def css_microservice():
    """
    (1) Runs continuously and checks css.txt for the 
        string "dark mode".
    (2) If the string is present, write the contents of 
        a css stylesheet with dark mode formatting to 
        css.txt.
    
    ** SOURCES **
    [material.io] 
        - for descriptions of readable color palettes and combinations for
        dark mode
    [compilezero.medium.com/dark-mode-ui-design-the-definitive-guide]
        - for hex codes of pre-made dark mode color palettes
    """
    
    # create a css.txt file in the cwd if it does not already exist
    new_file = open('./css.txt', 'w+')
    new_file.close()

    # define strings to hold condensed dark mode CSS files as text
    dark_mode_selection = ""
    dark_mode_purple = "img{filter:brightness(.85) contrast(1.15);}body{background-color:#18131E;color:#BB86FC;opacity:87%;}td,th{border-width:1px;border-style:solid;border-color:#F0F4F8;}tr:nth-child(even){background-color:#A155FF;color:#18131E}tr:hover{background-color:#BB86FC;color:#18131E;}th{background-color:#A155FF;color:#18131E;}h1,h2,h3,h4{font-weight:bolder;color:#BB86FC;}a{color:#BB86FC;}input{background-color:#BB86FC;color:#18131E;}input[type=button]{background-color:#C89BFF;color:#18131E;}"
    dark_mode_grey = "img{filter:brightness(.85) contrast(1.15);}body{background-color:#222222;color:#F7F7F7;opacity:87%;}td,th{border-width:1px;border-style:solid;border-color:#F7F7F7;}tr:nth-child(even){background-color:#3B3B3B}tr:hover{background-color:#CFCFCF;color:#222222;}th{background-color:#3B3B3B;color:#F7F7F7;}h1,h2,h3,h4{font-weight:bolder;color:#F7F7F7;}a{color:#E1E1E1;}input{background-color:#F7F7F7;color:#222222;}input[type=button]{background-color:#B1B1B1;color:#222222;}"
    dark_mode_blue ="img{filter:brightness(.85) contrast(1.15);}body{background-color:#102A43;color:#F0F4F8;opacity:87%;}td,th{border-width:1px;border-style:solid;border-color:#F0F4F8;}tr:nth-child(even){background-color:#486581}tr:hover{background-color:#D9E2Ec;color:#102A43;}th{background-color:#486581;color:#F0F4F8;}h1,h2,h3,h4{font-weight:bolder;color:#F0F4F8;}a{color:#E1E1E1;}input{background-color:#F0F4F8;color:#102A43;}input[type=button]{background-color:#9FB3C8;color:#102A43;}"
    
    while True:
        time.sleep(1)  # sleep for 1 second

        # continue checking 'css.txt' for one of the specified strings
        # 'dark mode', 'dark mode purple', or 'dark mode blue'
        with open('./css.txt', 'r') as service_file:
            file_line = service_file.readline().strip('\n').lower().strip()
            if file_line == 'dark mode':
                dark_mode_selection = dark_mode_grey
            elif file_line == 'dark mode purple':
                dark_mode_selection = dark_mode_purple
            elif file_line == 'dark mode blue':
                dark_mode_selection = dark_mode_blue
            else:
                service_file.close()
                continue  # continue looping until needed

        with open('./css.txt', 'w') as service_file:
            # write the dark mode css as text to 'css.txt', then close
            # the file and continue looping
            service_file.write(dark_mode_selection)
            service_file.close()

if __name__ == '__main__':
    css_microservice()