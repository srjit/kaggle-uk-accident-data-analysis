(TeX-add-style-hook
 "neu_handout"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "11pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "pdftex")))
   (TeX-run-style-hooks
    "article"
    "art11"
    "multirow"
    "graphicx")
   (TeX-add-symbols
    '("course" 2)
    "myInstitution"
    "myCourseCode"
    "myCourseTitle"
    "mySchoolLogo"))
 :latex)

