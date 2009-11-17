from commands import base, ls, wget, tar

cmdl = {
    '/bin/echo':        base.command_echo,
    'cd':               base.command_cd,
    '/bin/cat':         base.command_cat,
    '/usr/bin/whoami':  base.command_whoami,
    'quit':             base.command_quit,
    'exit':             base.command_quit,
    '/usr/bin/clear':   base.command_clear,
    '/bin/rm':          base.command_rm,
    '/usr/bin/uptime':  base.command_uptime,
    '/usr/bin/w':       base.command_w,
    '/usr/bin/who':     base.command_w,
    '/usr/bin/vi':      base.command_vi,
    '/usr/bin/vim':     base.command_vi,
    '/bin/mount':       base.command_mount,
    '/bin/pwd':         base.command_pwd,
    '/bin/uname':       base.command_uname,
    '/usr/bin/id':      base.command_id,
    '/usr/bin/passwd':  base.command_passwd,
    '/bin/mkdir':       base.command_mkdir,
    'set':              base.command_nop,
    'unset':            base.command_nop,
    'history':          base.command_nop,
    'export':           base.command_nop,
    '/bin/ls':          ls.command_ls,
    '/usr/bin/wget':    wget.command_wget,
    '/bin/tar':         tar.command_tar,
    }
