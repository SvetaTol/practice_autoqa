import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('svitlana_tolpinska')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('svitlana_tolpinska_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_visibility_email(github_api):
    r = github_api.visibility_email('sveta.tolpinskaya@gmail.com')
    assert r[0]['visibility'] == 'public'


@pytest.mark.api
def test_compare_commits(github_api):
    r = github_api.compare_commits('SvetaTol', 'practice_autoqa', 'main', 'one_more_branch')
    assert r['total_commits'] > 0


@pytest.mark.api
def test_privately_report_security_vulnerabilities(github_api):
    r = github_api.privately_report_security_vulnerabilities('SvetaTol', 'practice_autoqa')
    assert r['message'] == 'Not Found'