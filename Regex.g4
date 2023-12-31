grammar Regex;

regex
    : alternative ('|' alternative)*    # Alt
;

alternative
    : block*    # Cat
;

block
    : block '*'     # Rep
    | '(' regex ')' # Par
    | CHAR          # Chr
    | ESCAPE        # Esc
;

CHAR :
    ~[()*|\\]
;

ESCAPE :
    '\\' .
;
