# fixes limits
exec {'fix unlimit':
    command => 'sed -i s/15/1000/ /etc/default/nginx',
    path    => '/bin',
}
exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}