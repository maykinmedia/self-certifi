import os

import certifi

from self_certifi import load_self_signed_certs

CERTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certs")


def test_no_extra_certs(tmp_path, clean_environ):
    load_self_signed_certs(tmp_path)

    assert "REQUESTS_CA_BUNDLE" not in os.environ
    assert len([x for x in tmp_path.iterdir()]) == 0


def test_explicit_certs_list(tmp_path, clean_environ):
    certs = [
        os.path.join(CERTS_DIR, "root1.crt"),
        os.path.join(CERTS_DIR, "cert2.crt"),
    ]

    load_self_signed_certs(tmp_path, paths=certs)

    assert "REQUESTS_CA_BUNDLE" in os.environ
    bundle_file = os.environ["REQUESTS_CA_BUNDLE"]
    children = [str(x) for x in tmp_path.iterdir()]
    assert children == [bundle_file]

    with open(bundle_file) as infile:
        bundle = infile.read()

    for cert in certs:
        with open(cert) as cert_file:
            assert cert_file.read() in bundle

    with open(certifi.where()) as certifi_bundle:
        assert certifi_bundle.read() in bundle


def test_envvar_list(tmp_path, clean_environ):
    certs = [
        os.path.join(CERTS_DIR, "root1.crt"),
        os.path.join(CERTS_DIR, "cert2.crt"),
    ]
    clean_environ["EXTRA_VERIFY_CERTS"] = ",".join(certs)

    load_self_signed_certs(tmp_path)

    assert "REQUESTS_CA_BUNDLE" in os.environ
    bundle_file = os.environ["REQUESTS_CA_BUNDLE"]
    children = [str(x) for x in tmp_path.iterdir()]
    assert children == [bundle_file]

    with open(bundle_file) as infile:
        bundle = infile.read()

    for cert in certs:
        with open(cert) as cert_file:
            assert cert_file.read() in bundle

    with open(certifi.where()) as certifi_bundle:
        assert certifi_bundle.read() in bundle
