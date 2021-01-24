import sys
import requests

discogs_api_url = 'https://api.discogs.com/database'
token = 'irxlCkXntQUtuUzWqjkcFQPSbwKIRnQILfNENoHQ'

main_artist = input('Input the name of a group: ')

search = requests.get(discogs_api_url + '/search?q=' + main_artist + '&type=artist&token=' + token)
if search.status_code != 200:
    sys.exit('Invalid API response {0}.'.format(search['status']))

main_artist_id = search.json()['results'][0]['id']
main_artist_url = search.json()['results'][0]['resource_url']

main_artist_info = requests.get(main_artist_url)
if main_artist_info.status_code != 200:
    sys.exit('Invalid API response {0}.'.format(main_artist_info['status']))

artists_groups = {}
for item in main_artist_info.json()['members']:
    artist = item['name']
    artist_info = requests.get(item['resource_url'] + '?token=' + token)
    if artist_info.status_code != 200:
        sys.exit('Invalid API response {0}.'.format(artist_info['status']))
    for group in artist_info.json()['groups']:
        if group['id'] != main_artist_id:
            if group['name'] in artists_groups:
                if type(artists_groups[group['name']]) is str:
                    artists = [artists_groups[group['name']]]
                else:
                    artists = artists_groups[group['name']]
                artists.append(artist)
                artists_groups[group['name']] = artists
            else:
                artists_groups[group['name']] = artist

for x in artists_groups:
    if type(artists_groups[x]) is list:
        print('In group: "{}" played: {}'.format(x, artists_groups[x]))
