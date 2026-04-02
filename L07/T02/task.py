import requests
import hashlib
import sys

# Request hash suffix data from the Pwned Passwords API using the first 5 hash characters
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  # Send a GET request to the Pwned Passwords API and store the response
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

# Find the matching hash suffix in the API response and return its leak count
def get_password_leaks_count(hashes, hash_to_check):
  # Split the response text into lines and split each line into a hash suffix
  # and a leak count using `:` as the separator
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

# Check whether a password appears in known leaks by hashing it and querying the API
def pwned_api_check(password):
  # Encode the password as UTF-8, calculate its SHA-1 hash,
  # convert it to hex, and make it uppercase
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

# Check all passwords passed as command-line arguments and print the result for each one
def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

