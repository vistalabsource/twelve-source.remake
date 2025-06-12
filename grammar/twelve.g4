grammar twelve;

program: statement* EOF;
statement: printl;
printl: PRINTL EXPR SEMI;

// Lexer
PRINTL: 'printl';
EXPR: '"' (~[\r\n])* '"';
SEMI: ';';

WS: [ \t\r\n]+ -> skip; // Skip whitespace