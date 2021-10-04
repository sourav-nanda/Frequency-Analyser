
def credits():
    return '''
    <html>
    <head>
    
    <link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/vaakash/socializer/80391a50/css/socializer.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    
    </head>
    <body>
    
    <h3>Connect with me on </h3>
    <div class="socializer a sr-32px sr-opacity sr-icon-dark sr-bg-none sr-pad"><span class="sr-facebook"><a href="https://www.facebook.com/sourav.nanda.528" target="_blank" title="Facebook"><i class="fa fa-facebook"></i></a></span><span class="sr-instagram"><a href="https://www.instagram.com/_sourav_nanda_/?hl=en" target="_blank" title="Instagram"><i class="fa fa-instagram"></i></a></span><span class="sr-github"><a href="https://github.com/sourav-nanda/" target="_blank" title="Github"><i class="fa fa-github"></i></a></span><span class="sr-linkedin"><a href="https://www.linkedin.com/in/sourav-nanda-31ab841aa/" target="_blank" title="LinkedIn"><i class="fa fa-linkedin"></i></a></span></div>
    <div class="circleborder"><img class="face" src="https://avatars1.githubusercontent.com/u/67404111?s=400&u=179c2bd70de5b323c0fed27cf4e3bb3e697c7d0d&v=4" alt="face" width="56" height="56"></div>
    
    <style>
    .face {
    border-radius: 50%;}
    
    .circleborder {
    
    border: 10px silver;
    border-radius: 100%;
    display: inline-block;
    
    }
    <style>
    </body>
    </html> 
    '''
def max_width(size):

    return f"""
    <style>
    .reportview-container .main .block-container{{
        max-width: {size}px;
    }}
    </style>    
    """

def remove_table_index():
    return """
<style>
table td:nth-child(0) {
    display: none
}
table th:nth-child(1) {
    display: none
}
</style>
"""

def horizontal_table(chars,width):
    begin=f'''<table style="width: {width}%;">
	<tbody>
		<tr>'''

    end='''</tr>
        </tbody>
    </table>
'''

    body=''

    for char in chars:
        body+=f'<td style="width: 4%;">{char}</td>'


    return begin+body+end

def vertical_table(chars,width):
    cells=''

    for char in chars:
        cells+=f'<tr><td style="width: 100.0000%;">{char}</td></tr>'


    body=f'''<table style="width: {width}%;">
	<tbody>
		{cells}
	</tbody>
</table>'''

    return body
