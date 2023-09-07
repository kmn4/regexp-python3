# regexp-python3

## ANTLR

以下を準備

- antlr4-X.X.X-complete.jar
- antlr4-python3-runtime

具体的には以下のようにする。
`antlr4-tools` は JAR をダウンロードするためだけに使う。

```bash
pip install antlr4-tools
antlr4
pip uninstall antlr4-tools
pip install antlr4-python3-runtime
```

パーサの生成は以下の通り。

```bash
alias antlr4='java -Xmx500M -cp "$HOME/.m2/repository/org/antlr/antlr4/4.13.1/antlr4-4.13.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
antlr4 -Dlanguage=Python3 -o regex_parser -visitor -no-listener Regex.g4
```
