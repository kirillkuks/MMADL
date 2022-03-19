SET CLASSPATH=.;.\antlr-4.9-complete.jar;%CLASSPATH%

java org.antlr.v4.Tool -Dlanguage=Python3 MMADL.g4 -o ANTLR -visitor
