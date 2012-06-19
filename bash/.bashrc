

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

#if [ -f ~/.bash_aliases ]; then
#    . ~/.bash_aliases
#fi

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    eval "`dircolors -b`"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    #alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

# some more ls aliases
#alias ll='ls -l'
#alias la='ls -A'
#alias l='ls -CF'

alias sshlog='ssh root@10.18.102.186'
alias clojure='java -cp ~/.path/java/clojure.jar clojure.main'

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi
export PATH=/Users/shenchen/Documents/source/os/sys161/bin:/Users/shenchen/Documents/source/os/sys161/tools/bin:$PATH
export SVN_EDITOR=vim
export TOMCAT_HOME=/Applications/apache-tomcat-6.0.32
source ~/.git-completion.sh
source /Users/shenchen/Documents/github/misc/fastGo/go.sh
