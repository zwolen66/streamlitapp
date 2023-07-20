# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines and whitespace cleanup
[*]
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
insert_final_newline = true

# Protect whitespace in markdown files
[*.md]
trim_trailing_whitespace = false

# general formatting
[*.{go,sh,bash,zsh,Makefile}]
indent_style = tab
indent_size = 4

# Set default charset
[*.{html,xml,js,css,py}]
charset = utf-8

# python
[*.py]
indent_style = space
indent_size = 4

# webdev
[*.{html,xml,js,css}]
indent_style = space
indent_size = 2

