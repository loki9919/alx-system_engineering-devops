# Setup New Ubuntu server with nginx

exec { 'update_system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command => 'sed -i "24i\    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
