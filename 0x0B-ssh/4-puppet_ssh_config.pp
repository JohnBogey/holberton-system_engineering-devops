#edits etc config
file_line{'disable password login':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}

file_line{'add IdentityFile':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton',
}
