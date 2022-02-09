cat "$@" | tr '[:space:]' '\n' | tr '[:punct:]' '\n' | sed -e '/^ *$/d'
