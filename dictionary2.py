#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cgi, os
import csv
import difflib

f = open('wordlist2.csv', 'r')
data = csv.reader(f)

arguments = cgi.FieldStorage()
word_list = []
similar_words = []

for i in arguments.keys():
    x = arguments[i].value
    X = x.capitalize()

print "Content-type: text/html"
print
print '''<html><head>
<meta charset="utf-8">
    <title>Glossary</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,300,700" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/4.1.1/normalize.min.css">
    <link rel="stylesheet" href="http://bigcat.fhsu.edu/volgagerman/site.css">
</head>
<style>
.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #111;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}
.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color: #818181;
    display: block;
    transition: 0.3s
}
.sidenav a:hover, .offcanvas a:focus{
    color: #f1f1f1;
}
.closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px !important;
    margin-left: 50px;
}
@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
<body>
    <div id="container-mobile-left">

	  <img src="http://bigcat.fhsu.edu/volgagerman/sun.png" alt="Sun Flower Chapter logo" style="width:450px;height:75px;">  <img src="http://bigcat.fhsu.edu/volgagerman/khc.jpg" alt="Kansas Humanities Council logo" style="width:200px;height:75px;">  <img src="http://bigcat.fhsu.edu/volgagerman/fhsu.png" alt="FHSU logo" style="width:245px;height:90px;">
	<div id="mySidenav" class="sidenav">
	  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×</a>
	  <a href="http://bigcat.fhsu.edu/volgagerman/about.html">About</a>
	  <a href="http://bigcat.fhsu.edu/volgagerman/haberkorn/index.html">Haberkorn collection</a>
	  <a href="
	http://bigcat.fhsu.edu/volgagerman/songs.html">Song collection</a>
	  <a href="http://bigcat.fhsu.edu/cgi-bin/volgagerman/dictionary2.py">Glossary</a>
	  <a href="http://bigcat.fhsu.edu/volgagerman/grammar.html">Grammar</a>
	  <a href="http://bigcat.fhsu.edu/volgagerman/staff.html">Project staff</a>
	</div>
	<p></p>
	<span style="font-size:30px;cursor:pointer" onclick="openNav()">    ☰ menu
	</span>
	<script>
	function openNav() {
	    document.getElementById("mySidenav").style.width = "250px";
	}
	function closeNav() {
	    document.getElementById("mySidenav").style.width = "0";
	}
	</script>'''
print "<h1>Glossary</h1>"
print "<form>"
print "<input type='text' name='yyy'/>"
print "</form>"

for row in data:
    if x==row[0] or X==row[0]:
        word_list.append(row[0])
        print '<b> %s </b> (%s):' %(row[0], row[1])
        definitions = [ row[n] for n in range(3, len(row)) if row[n] != '' ]
        def_concatenated = '; '.join(definitions)
        print def_concatenated
        print '<br>'
        if row[2] is not '':
            print 'Standard German: ', row[2], '<br>'
    else:
        seq = difflib.SequenceMatcher(None, x, row[0])
        comp = seq.ratio()
        if comp > .80:
            similar_words.append(row[0])

if not word_list:
    print "Sorry, this word has not been added to the glossary yet. <br><br>"
    if similar_words:
        similar_words2 = []
        for word in similar_words:
            word = '''<a href="http://bigcat.fhsu.edu/cgi-bin/volgagerman/dictionary2.py?yyy=%s">%s</a>''' %(word, word)
            similar_words2.append(word)
        alternatives = ', '.join(similar_words2)
        print "Did you mean %s?" %(alternatives)

hab_dir = '/usr2/web/volgagerman/haberkorn'
os.chdir(hab_dir)
dirs = [name for name in os.listdir(".") if os.path.isdir(name)]

for d in dirs:
    path = hab_dir + '/' + d
    os.chdir(path)
    files = [name for name in os.listdir(".") if os.path.isfile(name)]
    example_list = []
    for f in files:
        if '_ger.txt' in f:
            f3 = open(f, 'r')
            data = f3.readlines()
            for i, j in enumerate(data):
                 if x in j or X in j:
                    print '<p>'
                    print '...'
                    try:
                        print data[i-4]
                    except:
                        pass
                    try:
                        print data[i-2]
                    except:
                        pass
                    new = '<b><font color="red">'+x+'</font></b>'
                    j = j.replace(x, new)
                    print j
                    try:
                        print data[i+2]
                    except:
                        pass
                    try:
                        print data[i+4]
                    except:
                        pass
                    print '...'

                    filename = '''https://bigcat.fhsu.edu/volgagerman/haberkorn/''' + d + '/' +d +'.html'
                    print '<br>'
                    print '<a href="%s">full text</a>' %(filename)
                    print '</p>'
    os.chdir(hab_dir)

print '''</body>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-71195923-2', 'auto');
  ga('send', 'pageview');
</script>
</html>'''
