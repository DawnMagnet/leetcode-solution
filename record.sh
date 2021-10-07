for f in $(find  .  -type f -regex  ".*.html")
do
    sed -i '31 a <script>\nvar _hmt = _hmt || [];\n(function() {\n  var hm = document.createElement("script");\n  hm.src = "https://hm.baidu.com/hm.js?68e5a42781c7cf226eb26bac2cf1a765";\n  var s = document.getElementsByTagName("script")[0]; \n  s.parentNode.insertBefore(hm, s);\n})();\n</script>' $f
done
