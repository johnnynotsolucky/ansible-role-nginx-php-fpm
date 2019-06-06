import os

import testinfra.utils.ansible_runner

# TODO

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_site_redirect(host):
    result = host.run((
        "curl "
        "-s "
        "--cacert /etc/test-certs/issuer.pem "
        "-I "
        "-H \"Host: test.dev\" "
        "localhost "
        "2>/dev/null "
        "| head -n1 "
    ))
    assert result.stdout == "HTTP/1.1 301 Moved Permanently\r\n"

    result = host.run((
        "curl "
        "-s "
        "--cacert /etc/test-certs/issuer.pem "
        "-I "
        "-H \"Host: test.dev\" "
        "localhost "
        "2>/dev/null "
        "| grep -E '^Location:' "
        "| awk '{print $2}'"))
    assert result.stdout == "https://test.dev/\r\n"


def test_site_tls(host):
    result = host.run((
        "curl "
        "-s "
        "--cacert /etc/test-certs/issuer.pem "
        "-I "
        "-H \"Host: test.dev\" "
        "https://localhost "
        "2>/dev/null "
        "| head -n 1 "
    ))
    assert result.stdout == "HTTP/2 200 \r\n"


def test_site_tls_redirect(host):
    result = host.run((
        "curl "
        "-s "
        "--cacert /etc/test-certs/issuer.pem "
        "-I "
        "-H \"Host: foo.test.dev\" "
        "https://localhost "
        "2>/dev/null "
        "| head -n1 "
    ))
    assert result.stdout == "HTTP/2 301 \r\n"

    result = host.run((
        "curl "
        "-s "
        "--cacert /etc/test-certs/issuer.pem "
        "-I "
        "-H \"Host: foo.test.dev\" "
        "localhost "
        "2>/dev/null "
        "| grep -E '^Location:' "
        "| awk '{print $2}'"))
    assert result.stdout == "https://test.dev/\r\n"
