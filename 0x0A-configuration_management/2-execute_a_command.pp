# Kill a process
exec { 'killmenow':
  path    => '/usr/bin/env',
  command => 'pkill -e killmenow'
  }
