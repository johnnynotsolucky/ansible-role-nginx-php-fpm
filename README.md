ansible-role-nginx-php-fpm
=========

Based on [http://github.com/geerlingguy/ansible-role-nginx/](http://github.com/geerlingguy/ansible-role-nginx/). Pre-configured to support php-fpm; Requires SSL certificates.

Requirements
------------

- PHP-FPM ([https://github.com/geerlingguy/ansible-role-php](https://github.com/geerlingguy/ansible-role-php))
- SSL Certificates

Role Variables
--------------

_TODO_

`nginx_ssl_certificate_path`
`nginx_ssl_certificate_key_path`
`nginx_ssl_trusted_certificate_path`


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    nginx_use_ppa: true
    server_name: "test.dev"
    nginx_ssl_certificate_path: "/etc/certs/client.cer"
    nginx_ssl_certificate_key_path: "/etc/certs/client.key"
    nginx_ssl_trusted_certificate_path: "/etc/certs/trusted.pem"
    php_enable_php_fpm: true
    php_fpm_listen: "/var/run/php/php7.3-fpm.sock"
    php_fpm_daemon: php7.3-fpm
    php_default_version_debian: 7.3
    php_enable_webserver: false
  roles:
    - role: geerlingguy.php
    - role: ansible-role-nginx-php-fpm
```

License
-------

MIT
