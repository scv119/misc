#################################
####    fast go dir #############
#################################

go_idx_path=~/.go_idx
if [ -f $go_idx_path ];then
    true
else
    touch $go_idx_path
fi

shownames(){
    sed -e 's/=[^=]*$//g' $go_idx_path
}

showpaths(){
    sed -e 's/^[^=]*=//g' $go_idx_path
}

goadd(){
    local bmpath=$(pwd)
    local bmname=''
    if [ $# -eq 1 ];then
        bmname=$1
    else
        echo "usage goadd KEY"
    fi
#    echo "$# $bmpath $bmname"
    
    if shownames|grep $bmname >>/dev/null; then
        echo "$bmname is already occupied"
        return
    fi

    echo "$bmname=$bmpath" >> $go_idx_path
}

golist(){
    cat $go_idx_path | sed -e 's/=/  /'
}

go(){
    if [ $# -eq 1 ]; then
        if shownames | grep $1 >>/dev/null; then
            matchone=$(grep $1 $go_idx_path)
            target=${matchone##*=}
            cd $target
        fi
    else
        echo 'usage go KEY'
    fi
}

godel(){
    for key in $@; do
        if shownames | grep $key >>/dev/null; then
            cat $go_idx_path | grep "$key="
            echo "is deleted"
            sed -i -e "/^${key}=/d" $go_idx_path
        fi
    done
}



################################
########## fast go end #########
################################

