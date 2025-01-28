# Оглавления
- [Что такое GIT?](#title1)
- [Кофигурация](#title2)
- [Commit](#commit)



# <a id="title1">Что такое GIT?</a>
1. Хранилище истории разработки
   - Просмотр и востановление
2. Обмен историей разработки
   - ![Обмен историей разработки](https://i.ytimg.com/vi/wDMR17qaTns/hqdefault.jpg)
3. Надежная система
   - История есть у всех

#### [Ссылка на YouTube видео](https://www.youtube.com/watch?v=W4hoc24K93E&list=PLDyvV36pndZFHXjXuwA_NywNrVQO0aQqb)

# <a id="title2">Кофигурация</a>

```git
git config -h
```
```GIT
usage: git config [<options>]

Config file location
    --[no-]global         use global config file
    --[no-]system         use system config file
    --[no-]local          use repository config file
    --[no-]worktree       use per-worktree config file
    -f, --[no-]file <file>
                          use given config file
    --[no-]blob <blob-id> read config from given blob object

Action
    --[no-]get            get value: name [value-pattern]
    --[no-]get-all        get all values: key [value-pattern]
    --[no-]get-regexp     get values for regexp: name-regex [value-pattern]
    --[no-]get-urlmatch   get value specific for the URL: section[.var] URL
    --[no-]replace-all    replace all matching variables: name value [value-pattern]
    --[no-]add            add a new variable: name value
    --[no-]unset          remove a variable: name [value-pattern]
    --[no-]unset-all      remove all matches: name [value-pattern]
    --[no-]rename-section rename section: old-name new-name
    --[no-]remove-section remove a section: name
    -l, --[no-]list       list all
    --[no-]fixed-value    use string equality when comparing values to 'value-pattern'
    -e, --[no-]edit       open an editor
    --[no-]get-color      find the color configured: slot [default]
    --[no-]get-colorbool  find the color setting: slot [stdout-is-tty]

Type
    -t, --[no-]type <type>
                          value is given this type
    --bool                value is "true" or "false"
    --int                 value is decimal number
    --bool-or-int         value is --bool or --int
    --bool-or-str         value is --bool or string
    --path                value is a path (file or directory name)
    --expiry-date         value is an expiry date

Other
    -z, --[no-]null       terminate values with NUL byte
    --[no-]name-only      show variable names only
    --[no-]includes       respect include directives on lookup
    --[no-]show-origin    show origin of config (file, standard input, blob, command line)
    --[no-]show-scope     show scope of config (worktree, local, global, system, command)
    --[no-]default <value>
                          with --get, use default value when missing entry
```

#### [Ссылка на YouTube видео](https://www.youtube.com/watch?v=hWiqh6YUUS8&list=PLDyvV36pndZFHXjXuwA_NywNrVQO0aQqb&index=2)

# Commit
```git
# Нулевой строкой (если работаешь в команде) к коммиту идет
git pull
# Эта строка переносит все изменения, которые вснесла команда
```
```git
# Первой строкой будет
git add filename
git add filename_1 filename_2 filename_3
git add .
# Эта строка добавляет файл/файлы в Index
```
```git
# Затем можно проветить статус репозитория
git status
```
```git
# Предследней строкой будет
git commit -m 'ваш комметарий к коммиту'
# Эта строка добавляет все изменения в репозиторий
```
```git
# Предпоследней строкой будет
git push
# Эта строка выгружает репозиторий на сервер
```