# Setting up my client config file

# turn off PasswordAuthentication
file_line { 'Turn off Password Authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

# Declare IdentityFile
file_line { 'Declare Identity File':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}