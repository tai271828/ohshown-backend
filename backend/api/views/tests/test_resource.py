import pytest
from ...models.const import OhshownEventConst

@pytest.mark.django_db
def test_get_ohshown_event_type_list(client):
    resp = client.get("/api/resources/ohshown-event-type")
    resp_json = resp.json()
    expect_list = OhshownEventConst.TYPE_LIST
    assert len(resp_json) == len(expect_list)
    for expect, actual in zip(expect_list, resp_json):
        assert expect[0] == actual['value']
        assert expect[1] == actual['text']
