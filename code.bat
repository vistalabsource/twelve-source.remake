@echo off
antlr4 -Dlanguage=Python3 -visitor -no-listener grammar/twelve.g4 -o src/Lexer_Parser