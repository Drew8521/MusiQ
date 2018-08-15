# -*- coding: utf-8 -*-

import json

pop = u'''{
  "items": [
    {
      "track": {
        "album": {
          "name": "High On Life (feat. Bonn)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/60d24wfXkVzDSfLS6hyCjZ"
            },
            "href": "https://api.spotify.com/v1/artists/60d24wfXkVzDSfLS6hyCjZ",
            "id": "60d24wfXkVzDSfLS6hyCjZ",
            "name": "Martin Garrix",
            "type": "artist",
            "uri": "spotify:artist:60d24wfXkVzDSfLS6hyCjZ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7Io0XduXk7aOHFHA7sLru2"
            },
            "href": "https://api.spotify.com/v1/artists/7Io0XduXk7aOHFHA7sLru2",
            "id": "7Io0XduXk7aOHFHA7sLru2",
            "name": "Bonn",
            "type": "artist",
            "uri": "spotify:artist:7Io0XduXk7aOHFHA7sLru2"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4ut5G4rgB1ClpMTMfjoIuy"
        },
        "name": "High On Life (feat. Bonn)"
      }
    },
    {
      "track": {
        "album": {
          "name": "One Kiss (with Dua Lipa) [Remixes]"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7CajNmpbOovFoOoasH2HaY"
            },
            "href": "https://api.spotify.com/v1/artists/7CajNmpbOovFoOoasH2HaY",
            "id": "7CajNmpbOovFoOoasH2HaY",
            "name": "Calvin Harris",
            "type": "artist",
            "uri": "spotify:artist:7CajNmpbOovFoOoasH2HaY"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6M2wZ9GZgrQXHCFfjv46we"
            },
            "href": "https://api.spotify.com/v1/artists/6M2wZ9GZgrQXHCFfjv46we",
            "id": "6M2wZ9GZgrQXHCFfjv46we",
            "name": "Dua Lipa",
            "type": "artist",
            "uri": "spotify:artist:6M2wZ9GZgrQXHCFfjv46we"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5nki7yRhxgM509M5ADlN1p"
            },
            "href": "https://api.spotify.com/v1/artists/5nki7yRhxgM509M5ADlN1p",
            "id": "5nki7yRhxgM509M5ADlN1p",
            "name": "Oliver Heldens",
            "type": "artist",
            "uri": "spotify:artist:5nki7yRhxgM509M5ADlN1p"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7b4vbqgzMhbFa0wdjfftQJ"
        },
        "name": "One Kiss (with Dua Lipa) - Oliver Heldens Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "Jackie Chan"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2o5jDhtHVPhrJdv3cEQ99Z"
            },
            "href": "https://api.spotify.com/v1/artists/2o5jDhtHVPhrJdv3cEQ99Z",
            "id": "2o5jDhtHVPhrJdv3cEQ99Z",
            "name": "Tiësto",
            "type": "artist",
            "uri": "spotify:artist:2o5jDhtHVPhrJdv3cEQ99Z"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5vQfv3s2Z2SRdPZKr82ABw"
            },
            "href": "https://api.spotify.com/v1/artists/5vQfv3s2Z2SRdPZKr82ABw",
            "id": "5vQfv3s2Z2SRdPZKr82ABw",
            "name": "Dzeko",
            "type": "artist",
            "uri": "spotify:artist:5vQfv3s2Z2SRdPZKr82ABw"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0bdJZl7TDeiymDYzMJnVh2"
            },
            "href": "https://api.spotify.com/v1/artists/0bdJZl7TDeiymDYzMJnVh2",
            "id": "0bdJZl7TDeiymDYzMJnVh2",
            "name": "Preme",
            "type": "artist",
            "uri": "spotify:artist:0bdJZl7TDeiymDYzMJnVh2"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/246dkjvS1zLTtiykXe5h60"
            },
            "href": "https://api.spotify.com/v1/artists/246dkjvS1zLTtiykXe5h60",
            "id": "246dkjvS1zLTtiykXe5h60",
            "name": "Post Malone",
            "type": "artist",
            "uri": "spotify:artist:246dkjvS1zLTtiykXe5h60"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4kWO6O1BUXcZmaxitpVUwp"
        },
        "name": "Jackie Chan"
      }
    },
    {
      "track": {
        "album": {
          "name": "Ocean (feat. Khalid) [Don Diablo Remix]"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/60d24wfXkVzDSfLS6hyCjZ"
            },
            "href": "https://api.spotify.com/v1/artists/60d24wfXkVzDSfLS6hyCjZ",
            "id": "60d24wfXkVzDSfLS6hyCjZ",
            "name": "Martin Garrix",
            "type": "artist",
            "uri": "spotify:artist:60d24wfXkVzDSfLS6hyCjZ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1l2ekx5skC4gJH8djERwh1"
            },
            "href": "https://api.spotify.com/v1/artists/1l2ekx5skC4gJH8djERwh1",
            "id": "1l2ekx5skC4gJH8djERwh1",
            "name": "Don Diablo",
            "type": "artist",
            "uri": "spotify:artist:1l2ekx5skC4gJH8djERwh1"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny"
            },
            "href": "https://api.spotify.com/v1/artists/6LuN9FCkKOj5PcnpouEgny",
            "id": "6LuN9FCkKOj5PcnpouEgny",
            "name": "Khalid",
            "type": "artist",
            "uri": "spotify:artist:6LuN9FCkKOj5PcnpouEgny"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4oOQ5XZuR4ywDje9SjiA7d"
        },
        "name": "Ocean (feat. Khalid) - Don Diablo Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "Your Love"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1Cs0zKBU1kc0i8ypK3B9ai"
            },
            "href": "https://api.spotify.com/v1/artists/1Cs0zKBU1kc0i8ypK3B9ai",
            "id": "1Cs0zKBU1kc0i8ypK3B9ai",
            "name": "David Guetta",
            "type": "artist",
            "uri": "spotify:artist:1Cs0zKBU1kc0i8ypK3B9ai"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3gk0OYeLFWYupGFRHqLSR7"
            },
            "href": "https://api.spotify.com/v1/artists/3gk0OYeLFWYupGFRHqLSR7",
            "id": "3gk0OYeLFWYupGFRHqLSR7",
            "name": "Showtek",
            "type": "artist",
            "uri": "spotify:artist:3gk0OYeLFWYupGFRHqLSR7"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0tgbSxoFjZ20MjfoKwWevV"
        },
        "name": "Your Love"
      }
    },
    {
      "track": {
        "album": {
          "name": "Panic Room"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1eMmoIprPDWeFdB1FxU6ZV"
            },
            "href": "https://api.spotify.com/v1/artists/1eMmoIprPDWeFdB1FxU6ZV",
            "id": "1eMmoIprPDWeFdB1FxU6ZV",
            "name": "Au/Ra",
            "type": "artist",
            "uri": "spotify:artist:1eMmoIprPDWeFdB1FxU6ZV"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/240wlM8vDrf6S4zCyzGj2W"
            },
            "href": "https://api.spotify.com/v1/artists/240wlM8vDrf6S4zCyzGj2W",
            "id": "240wlM8vDrf6S4zCyzGj2W",
            "name": "CamelPhat",
            "type": "artist",
            "uri": "spotify:artist:240wlM8vDrf6S4zCyzGj2W"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3MkuFR7t25mu7Iscp6GGiV"
        },
        "name": "Panic Room"
      }
    },
    {
      "track": {
        "album": {
          "name": "Heaven To Me"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1l2ekx5skC4gJH8djERwh1"
            },
            "href": "https://api.spotify.com/v1/artists/1l2ekx5skC4gJH8djERwh1",
            "id": "1l2ekx5skC4gJH8djERwh1",
            "name": "Don Diablo",
            "type": "artist",
            "uri": "spotify:artist:1l2ekx5skC4gJH8djERwh1"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5Tf4EH8tDvznnjULcFxkIl"
            },
            "href": "https://api.spotify.com/v1/artists/5Tf4EH8tDvznnjULcFxkIl",
            "id": "5Tf4EH8tDvznnjULcFxkIl",
            "name": "Alex Clare",
            "type": "artist",
            "uri": "spotify:artist:5Tf4EH8tDvznnjULcFxkIl"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1kU6Ypa94r15TPdXiCPwqS"
        },
        "name": "Heaven To Me"
      }
    },
    {
      "track": {
        "album": {
          "name": "Body (Remixes)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6t1gpxYbY8OlLA7D2RiikQ"
            },
            "href": "https://api.spotify.com/v1/artists/6t1gpxYbY8OlLA7D2RiikQ",
            "id": "6t1gpxYbY8OlLA7D2RiikQ",
            "name": "Loud Luxury",
            "type": "artist",
            "uri": "spotify:artist:6t1gpxYbY8OlLA7D2RiikQ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/58xvIqMyzvPuxxGODQSA0u"
            },
            "href": "https://api.spotify.com/v1/artists/58xvIqMyzvPuxxGODQSA0u",
            "id": "58xvIqMyzvPuxxGODQSA0u",
            "name": "brando",
            "type": "artist",
            "uri": "spotify:artist:58xvIqMyzvPuxxGODQSA0u"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0dQxAPdnh401uTrrX0vg7m"
        },
        "name": "Body"
      }
    },
    {
      "track": {
        "album": {
          "name": "Dancing Alone"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2XnBwblw31dfGnspMIwgWz"
            },
            "href": "https://api.spotify.com/v1/artists/2XnBwblw31dfGnspMIwgWz",
            "id": "2XnBwblw31dfGnspMIwgWz",
            "name": "Axwell / Ingrosso",
            "type": "artist",
            "uri": "spotify:artist:2XnBwblw31dfGnspMIwgWz"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4b8dLpJgJpNQYzu4AtXLt3"
            },
            "href": "https://api.spotify.com/v1/artists/4b8dLpJgJpNQYzu4AtXLt3",
            "id": "4b8dLpJgJpNQYzu4AtXLt3",
            "name": "RØMANS",
            "type": "artist",
            "uri": "spotify:artist:4b8dLpJgJpNQYzu4AtXLt3"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5xzzxWj8a1YBbNZhNLqWuQ"
        },
        "name": "Dancing Alone"
      }
    },
    {
      "track": {
        "album": {
          "name": "17"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1yqxFtPHKcGcv6SXZNdyT9"
            },
            "href": "https://api.spotify.com/v1/artists/1yqxFtPHKcGcv6SXZNdyT9",
            "id": "1yqxFtPHKcGcv6SXZNdyT9",
            "name": "MK",
            "type": "artist",
            "uri": "spotify:artist:1yqxFtPHKcGcv6SXZNdyT9"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/15DwFznkBJir7AK9PyMyRR"
        },
        "name": "17"
      }
    },
    {
      "track": {
        "album": {
          "name": "Born To Be Yours"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/23fqKkggKUBHNkbKtXEls4"
            },
            "href": "https://api.spotify.com/v1/artists/23fqKkggKUBHNkbKtXEls4",
            "id": "23fqKkggKUBHNkbKtXEls4",
            "name": "Kygo",
            "type": "artist",
            "uri": "spotify:artist:23fqKkggKUBHNkbKtXEls4"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q"
            },
            "href": "https://api.spotify.com/v1/artists/53XhwfbYqKCa1cC15pYq2q",
            "id": "53XhwfbYqKCa1cC15pYq2q",
            "name": "Imagine Dragons",
            "type": "artist",
            "uri": "spotify:artist:53XhwfbYqKCa1cC15pYq2q"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0kHyKhJMukHEPfeh8s7rdM"
        },
        "name": "Born To Be Yours"
      }
    },
    {
      "track": {
        "album": {
          "name": "AVICI (01)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
            },
            "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
            "id": "1vCWHaC5f2uS3yhpwWbIA6",
            "name": "Avicii",
            "type": "artist",
            "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5JYo7gm2dkyLLlWHjxS7Dy"
            },
            "href": "https://api.spotify.com/v1/artists/5JYo7gm2dkyLLlWHjxS7Dy",
            "id": "5JYo7gm2dkyLLlWHjxS7Dy",
            "name": "Sandro Cavazza",
            "type": "artist",
            "uri": "spotify:artist:5JYo7gm2dkyLLlWHjxS7Dy"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6Pgkp4qUoTmJIPn7ReaGxL"
        },
        "name": "Without You (feat. Sandro Cavazza)"
      }
    },
    {
      "track": {
        "album": {
          "name": "Tim"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1rSGNXhhYuWoq9BEz5DZGO"
            },
            "href": "https://api.spotify.com/v1/artists/1rSGNXhhYuWoq9BEz5DZGO",
            "id": "1rSGNXhhYuWoq9BEz5DZGO",
            "name": "ARTY",
            "type": "artist",
            "uri": "spotify:artist:1rSGNXhhYuWoq9BEz5DZGO"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4wmrfUPuvK9phVehREZZ1X"
        },
        "name": "Tim"
      }
    },
    {
      "track": {
        "album": {
          "name": "Alone (Calvin Harris Remix) (Feat. Stefflon Don)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/26VFTg2z8YR0cCuwLzESi2"
            },
            "href": "https://api.spotify.com/v1/artists/26VFTg2z8YR0cCuwLzESi2",
            "id": "26VFTg2z8YR0cCuwLzESi2",
            "name": "Halsey",
            "type": "artist",
            "uri": "spotify:artist:26VFTg2z8YR0cCuwLzESi2"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2ExGrw6XpbtUAJHTLtUXUD"
            },
            "href": "https://api.spotify.com/v1/artists/2ExGrw6XpbtUAJHTLtUXUD",
            "id": "2ExGrw6XpbtUAJHTLtUXUD",
            "name": "Stefflon Don",
            "type": "artist",
            "uri": "spotify:artist:2ExGrw6XpbtUAJHTLtUXUD"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7CajNmpbOovFoOoasH2HaY"
            },
            "href": "https://api.spotify.com/v1/artists/7CajNmpbOovFoOoasH2HaY",
            "id": "7CajNmpbOovFoOoasH2HaY",
            "name": "Calvin Harris",
            "type": "artist",
            "uri": "spotify:artist:7CajNmpbOovFoOoasH2HaY"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5K09638EBQjVMrZYXA89aC"
        },
        "name": "Alone (Calvin Harris Remix) (Feat. Stefflon Don)"
      }
    },
    {
      "track": {
        "album": {
          "name": "The Middle"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2qxJFvFYMEDqd7ui6kSAcq"
            },
            "href": "https://api.spotify.com/v1/artists/2qxJFvFYMEDqd7ui6kSAcq",
            "id": "2qxJFvFYMEDqd7ui6kSAcq",
            "name": "Zedd",
            "type": "artist",
            "uri": "spotify:artist:2qxJFvFYMEDqd7ui6kSAcq"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6WY7D3jk8zTrHtmkqqo5GI"
            },
            "href": "https://api.spotify.com/v1/artists/6WY7D3jk8zTrHtmkqqo5GI",
            "id": "6WY7D3jk8zTrHtmkqqo5GI",
            "name": "Maren Morris",
            "type": "artist",
            "uri": "spotify:artist:6WY7D3jk8zTrHtmkqqo5GI"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4lDBihdpMlOalxy1jkUbPl"
            },
            "href": "https://api.spotify.com/v1/artists/4lDBihdpMlOalxy1jkUbPl",
            "id": "4lDBihdpMlOalxy1jkUbPl",
            "name": "Grey",
            "type": "artist",
            "uri": "spotify:artist:4lDBihdpMlOalxy1jkUbPl"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/09IStsImFySgyp0pIQdqAc"
        },
        "name": "The Middle"
      }
    },
    {
      "track": {
        "album": {
          "name": "Another Chance (Don Diablo Edit)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/364ge6OLf1AsRisexSjfJN"
            },
            "href": "https://api.spotify.com/v1/artists/364ge6OLf1AsRisexSjfJN",
            "id": "364ge6OLf1AsRisexSjfJN",
            "name": "Big Pineapple",
            "type": "artist",
            "uri": "spotify:artist:364ge6OLf1AsRisexSjfJN"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1l2ekx5skC4gJH8djERwh1"
            },
            "href": "https://api.spotify.com/v1/artists/1l2ekx5skC4gJH8djERwh1",
            "id": "1l2ekx5skC4gJH8djERwh1",
            "name": "Don Diablo",
            "type": "artist",
            "uri": "spotify:artist:1l2ekx5skC4gJH8djERwh1"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1VTvqPZc50yS6MiWw520Kh"
        },
        "name": "Another Chance (Don Diablo Edit)"
      }
    },
    {
      "track": {
        "album": {
          "name": "Flames"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1Cs0zKBU1kc0i8ypK3B9ai"
            },
            "href": "https://api.spotify.com/v1/artists/1Cs0zKBU1kc0i8ypK3B9ai",
            "id": "1Cs0zKBU1kc0i8ypK3B9ai",
            "name": "David Guetta",
            "type": "artist",
            "uri": "spotify:artist:1Cs0zKBU1kc0i8ypK3B9ai"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5WUlDfRSoLAfcVSX1WnrxN"
            },
            "href": "https://api.spotify.com/v1/artists/5WUlDfRSoLAfcVSX1WnrxN",
            "id": "5WUlDfRSoLAfcVSX1WnrxN",
            "name": "Sia",
            "type": "artist",
            "uri": "spotify:artist:5WUlDfRSoLAfcVSX1WnrxN"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1mvghSCONexEGEuSJVbnsT"
        },
        "name": "Flames - David Guetta Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "True"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
            },
            "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
            "id": "1vCWHaC5f2uS3yhpwWbIA6",
            "name": "Avicii",
            "type": "artist",
            "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4h8VwCb1MTGoLKueQ1WgbD"
        },
        "name": "Wake Me Up - Radio Edit"
      }
    },
    {
      "track": {
        "album": {
          "name": "Like I Do"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1Cs0zKBU1kc0i8ypK3B9ai"
            },
            "href": "https://api.spotify.com/v1/artists/1Cs0zKBU1kc0i8ypK3B9ai",
            "id": "1Cs0zKBU1kc0i8ypK3B9ai",
            "name": "David Guetta",
            "type": "artist",
            "uri": "spotify:artist:1Cs0zKBU1kc0i8ypK3B9ai"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/60d24wfXkVzDSfLS6hyCjZ"
            },
            "href": "https://api.spotify.com/v1/artists/60d24wfXkVzDSfLS6hyCjZ",
            "id": "60d24wfXkVzDSfLS6hyCjZ",
            "name": "Martin Garrix",
            "type": "artist",
            "uri": "spotify:artist:60d24wfXkVzDSfLS6hyCjZ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4mHAu7NX2UNsnGXjviBD9e"
            },
            "href": "https://api.spotify.com/v1/artists/4mHAu7NX2UNsnGXjviBD9e",
            "id": "4mHAu7NX2UNsnGXjviBD9e",
            "name": "Brooks",
            "type": "artist",
            "uri": "spotify:artist:4mHAu7NX2UNsnGXjviBD9e"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6RnkFd8Fqqgk1Uni8RgqCQ"
        },
        "name": "Like I Do"
      }
    },
    {
      "track": {
        "album": {
          "name": "Who You Are (Remixes)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6i1GVNJCyyssRwXmnaeEFH"
            },
            "href": "https://api.spotify.com/v1/artists/6i1GVNJCyyssRwXmnaeEFH",
            "id": "6i1GVNJCyyssRwXmnaeEFH",
            "name": "Syn Cole",
            "type": "artist",
            "uri": "spotify:artist:6i1GVNJCyyssRwXmnaeEFH"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2G0xaYcKwIaY0i6FDAVbpU"
        },
        "name": "Who You Are (feat. MIO)"
      }
    },
    {
      "track": {
        "album": {
          "name": "More Than You Know"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2XnBwblw31dfGnspMIwgWz"
            },
            "href": "https://api.spotify.com/v1/artists/2XnBwblw31dfGnspMIwgWz",
            "id": "2XnBwblw31dfGnspMIwgWz",
            "name": "Axwell / Ingrosso",
            "type": "artist",
            "uri": "spotify:artist:2XnBwblw31dfGnspMIwgWz"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6h5PAsRni4IRlxWr6uDPTP"
        },
        "name": "More Than You Know"
      }
    },
    {
      "track": {
        "album": {
          "name": "Finest Hour (feat. Abir)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1LOB7jTeEV14pHai6EXSzF"
            },
            "href": "https://api.spotify.com/v1/artists/1LOB7jTeEV14pHai6EXSzF",
            "id": "1LOB7jTeEV14pHai6EXSzF",
            "name": "Cash Cash",
            "type": "artist",
            "uri": "spotify:artist:1LOB7jTeEV14pHai6EXSzF"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3QUOtWgmuxFyae4C0Q0thd"
            },
            "href": "https://api.spotify.com/v1/artists/3QUOtWgmuxFyae4C0Q0thd",
            "id": "3QUOtWgmuxFyae4C0Q0thd",
            "name": "Abir",
            "type": "artist",
            "uri": "spotify:artist:3QUOtWgmuxFyae4C0Q0thd"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0p0ljM6RxgpGt7wthGqBZa"
        },
        "name": "Finest Hour (feat. Abir)"
      }
    },
    {
      "track": {
        "album": {
          "name": "Satisfied (feat. MAX) & Mama Look At Me Now"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4sTQVOfp9vEMCemLw50sbu"
            },
            "href": "https://api.spotify.com/v1/artists/4sTQVOfp9vEMCemLw50sbu",
            "id": "4sTQVOfp9vEMCemLw50sbu",
            "name": "Galantis",
            "type": "artist",
            "uri": "spotify:artist:4sTQVOfp9vEMCemLw50sbu"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5UaEBgRvUPFf5CEDhaTdp7"
        },
        "name": "Mama Look At Me Now"
      }
    },
    {
      "track": {
        "album": {
          "name": "Audio (CID Remix)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5WUlDfRSoLAfcVSX1WnrxN"
            },
            "href": "https://api.spotify.com/v1/artists/5WUlDfRSoLAfcVSX1WnrxN",
            "id": "5WUlDfRSoLAfcVSX1WnrxN",
            "name": "Sia",
            "type": "artist",
            "uri": "spotify:artist:5WUlDfRSoLAfcVSX1WnrxN"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5fMUXHkw8R8eOP2RNVYEZX"
            },
            "href": "https://api.spotify.com/v1/artists/5fMUXHkw8R8eOP2RNVYEZX",
            "id": "5fMUXHkw8R8eOP2RNVYEZX",
            "name": "Diplo",
            "type": "artist",
            "uri": "spotify:artist:5fMUXHkw8R8eOP2RNVYEZX"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2feDdbD5araYcm6JhFHHw7"
            },
            "href": "https://api.spotify.com/v1/artists/2feDdbD5araYcm6JhFHHw7",
            "id": "2feDdbD5araYcm6JhFHHw7",
            "name": "Labrinth",
            "type": "artist",
            "uri": "spotify:artist:2feDdbD5araYcm6JhFHHw7"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6IZ4ctovY9dl7bgHClAvKJ"
            },
            "href": "https://api.spotify.com/v1/artists/6IZ4ctovY9dl7bgHClAvKJ",
            "id": "6IZ4ctovY9dl7bgHClAvKJ",
            "name": "LSD",
            "type": "artist",
            "uri": "spotify:artist:6IZ4ctovY9dl7bgHClAvKJ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4FCzCS0KEgb0rgySWINItO"
            },
            "href": "https://api.spotify.com/v1/artists/4FCzCS0KEgb0rgySWINItO",
            "id": "4FCzCS0KEgb0rgySWINItO",
            "name": "CID",
            "type": "artist",
            "uri": "spotify:artist:4FCzCS0KEgb0rgySWINItO"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3ajiUFrVUHsmU5F2pv3kzd"
        },
        "name": "Audio - CID Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "Darkside"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7vk5e3vY1uw9plTHJAMwjN"
            },
            "href": "https://api.spotify.com/v1/artists/7vk5e3vY1uw9plTHJAMwjN",
            "id": "7vk5e3vY1uw9plTHJAMwjN",
            "name": "Alan Walker",
            "type": "artist",
            "uri": "spotify:artist:7vk5e3vY1uw9plTHJAMwjN"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1eMmoIprPDWeFdB1FxU6ZV"
            },
            "href": "https://api.spotify.com/v1/artists/1eMmoIprPDWeFdB1FxU6ZV",
            "id": "1eMmoIprPDWeFdB1FxU6ZV",
            "name": "Au/Ra",
            "type": "artist",
            "uri": "spotify:artist:1eMmoIprPDWeFdB1FxU6ZV"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6064pL9Hu3Wx2bwJMeOx6o"
            },
            "href": "https://api.spotify.com/v1/artists/6064pL9Hu3Wx2bwJMeOx6o",
            "id": "6064pL9Hu3Wx2bwJMeOx6o",
            "name": "Tomine Harket",
            "type": "artist",
            "uri": "spotify:artist:6064pL9Hu3Wx2bwJMeOx6o"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1snWlbcbgQpJfknoI30DWG"
        },
        "name": "Darkside"
      }
    },
    {
      "track": {
        "album": {
          "name": "Sick Boy...Side Effects"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp"
            },
            "href": "https://api.spotify.com/v1/artists/69GGBxA162lTqCwzJG5jLp",
            "id": "69GGBxA162lTqCwzJG5jLp",
            "name": "The Chainsmokers",
            "type": "artist",
            "uri": "spotify:artist:69GGBxA162lTqCwzJG5jLp"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1oKdM70mJD8VvDOTKeS8t1"
            },
            "href": "https://api.spotify.com/v1/artists/1oKdM70mJD8VvDOTKeS8t1",
            "id": "1oKdM70mJD8VvDOTKeS8t1",
            "name": "Emily Warren",
            "type": "artist",
            "uri": "spotify:artist:1oKdM70mJD8VvDOTKeS8t1"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5yNEdBlZMxpcVtGKz5NFk5"
        },
        "name": "Side Effects"
      }
    },
    {
      "track": {
        "album": {
          "name": "Sunrise"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1rSGNXhhYuWoq9BEz5DZGO"
            },
            "href": "https://api.spotify.com/v1/artists/1rSGNXhhYuWoq9BEz5DZGO",
            "id": "1rSGNXhhYuWoq9BEz5DZGO",
            "name": "ARTY",
            "type": "artist",
            "uri": "spotify:artist:1rSGNXhhYuWoq9BEz5DZGO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4nEs5Ln0E5g3UtNu8suntA"
            },
            "href": "https://api.spotify.com/v1/artists/4nEs5Ln0E5g3UtNu8suntA",
            "id": "4nEs5Ln0E5g3UtNu8suntA",
            "name": "April Bender",
            "type": "artist",
            "uri": "spotify:artist:4nEs5Ln0E5g3UtNu8suntA"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7vLIj2GVAeYrohv8p0JjF0"
        },
        "name": "Sunrise"
      }
    },
    {
      "track": {
        "album": {
          "name": "Rise"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1HBjj22wzbscIZ9sEb5dyf"
            },
            "href": "https://api.spotify.com/v1/artists/1HBjj22wzbscIZ9sEb5dyf",
            "id": "1HBjj22wzbscIZ9sEb5dyf",
            "name": "Jonas Blue",
            "type": "artist",
            "uri": "spotify:artist:1HBjj22wzbscIZ9sEb5dyf"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1INuLZXjjVbcJRyWvD1iSq"
            },
            "href": "https://api.spotify.com/v1/artists/1INuLZXjjVbcJRyWvD1iSq",
            "id": "1INuLZXjjVbcJRyWvD1iSq",
            "name": "Jack & Jack",
            "type": "artist",
            "uri": "spotify:artist:1INuLZXjjVbcJRyWvD1iSq"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3u1S1OmAUhx5DRlLrXqyp3"
        },
        "name": "Rise"
      }
    },
    {
      "track": {
        "album": {
          "name": "Lullaby"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1IueXOQyABrMOprrzwQJWN"
            },
            "href": "https://api.spotify.com/v1/artists/1IueXOQyABrMOprrzwQJWN",
            "id": "1IueXOQyABrMOprrzwQJWN",
            "name": "Sigala",
            "type": "artist",
            "uri": "spotify:artist:1IueXOQyABrMOprrzwQJWN"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4fwuXg6XQHfdlOdmw36OHa"
            },
            "href": "https://api.spotify.com/v1/artists/4fwuXg6XQHfdlOdmw36OHa",
            "id": "4fwuXg6XQHfdlOdmw36OHa",
            "name": "Paloma Faith",
            "type": "artist",
            "uri": "spotify:artist:4fwuXg6XQHfdlOdmw36OHa"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5xzCzOAOfRi4DOttSzvznR"
        },
        "name": "Lullaby"
      }
    },
    {
      "track": {
        "album": {
          "name": "Let's Get Ill"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/540vIaP2JwjQb9dm3aArA4"
            },
            "href": "https://api.spotify.com/v1/artists/540vIaP2JwjQb9dm3aArA4",
            "id": "540vIaP2JwjQb9dm3aArA4",
            "name": "DJ Snake",
            "type": "artist",
            "uri": "spotify:artist:540vIaP2JwjQb9dm3aArA4"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7aSsnDTH11xS2yIn6cNtsF"
            },
            "href": "https://api.spotify.com/v1/artists/7aSsnDTH11xS2yIn6cNtsF",
            "id": "7aSsnDTH11xS2yIn6cNtsF",
            "name": "Mercer",
            "type": "artist",
            "uri": "spotify:artist:7aSsnDTH11xS2yIn6cNtsF"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3J5AcWRzmgbq4svZt91l3e"
        },
        "name": "Let's Get Ill"
      }
    },
    {
      "track": {
        "album": {
          "name": "I Could Be Wrong"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5wwneIFdawNgQ7GvKK29Z3"
            },
            "href": "https://api.spotify.com/v1/artists/5wwneIFdawNgQ7GvKK29Z3",
            "id": "5wwneIFdawNgQ7GvKK29Z3",
            "name": "Lucas & Steve",
            "type": "artist",
            "uri": "spotify:artist:5wwneIFdawNgQ7GvKK29Z3"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/05oH07COxkXKIMt6mIPRee"
            },
            "href": "https://api.spotify.com/v1/artists/05oH07COxkXKIMt6mIPRee",
            "id": "05oH07COxkXKIMt6mIPRee",
            "name": "Brandy",
            "type": "artist",
            "uri": "spotify:artist:05oH07COxkXKIMt6mIPRee"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7BF5rE2EVDmWNXc0uoP8Bz"
        },
        "name": "I Could Be Wrong"
      }
    },
    {
      "track": {
        "album": {
          "name": "Changa"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6n28c9qs9hNGriNa72b26u"
            },
            "href": "https://api.spotify.com/v1/artists/6n28c9qs9hNGriNa72b26u",
            "id": "6n28c9qs9hNGriNa72b26u",
            "name": "Pnau",
            "type": "artist",
            "uri": "spotify:artist:6n28c9qs9hNGriNa72b26u"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/59Yq0xrABEihHANsfo9QMT"
            },
            "href": "https://api.spotify.com/v1/artists/59Yq0xrABEihHANsfo9QMT",
            "id": "59Yq0xrABEihHANsfo9QMT",
            "name": "Blanke",
            "type": "artist",
            "uri": "spotify:artist:59Yq0xrABEihHANsfo9QMT"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5TL9e2xgtvJFtNCBsq1CgX"
        },
        "name": "Changa - Blanke Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "Anthem"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5vQfv3s2Z2SRdPZKr82ABw"
            },
            "href": "https://api.spotify.com/v1/artists/5vQfv3s2Z2SRdPZKr82ABw",
            "id": "5vQfv3s2Z2SRdPZKr82ABw",
            "name": "Dzeko",
            "type": "artist",
            "uri": "spotify:artist:5vQfv3s2Z2SRdPZKr82ABw"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2paaWadjhhY3shymyR5TcH"
            },
            "href": "https://api.spotify.com/v1/artists/2paaWadjhhY3shymyR5TcH",
            "id": "2paaWadjhhY3shymyR5TcH",
            "name": "Riggi & Piros",
            "type": "artist",
            "uri": "spotify:artist:2paaWadjhhY3shymyR5TcH"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/11NW0Oxsyz8anQlRuIOV0g"
        },
        "name": "Anthem"
      }
    },
    {
      "track": {
        "album": {
          "name": "FRIENDS (Borgeous Remix)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/64KEffDW9EtZ1y2vBYgq8T"
            },
            "href": "https://api.spotify.com/v1/artists/64KEffDW9EtZ1y2vBYgq8T",
            "id": "64KEffDW9EtZ1y2vBYgq8T",
            "name": "Marshmello",
            "type": "artist",
            "uri": "spotify:artist:64KEffDW9EtZ1y2vBYgq8T"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1zNqDE7qDGCsyzJwohVaoX"
            },
            "href": "https://api.spotify.com/v1/artists/1zNqDE7qDGCsyzJwohVaoX",
            "id": "1zNqDE7qDGCsyzJwohVaoX",
            "name": "Anne-Marie",
            "type": "artist",
            "uri": "spotify:artist:1zNqDE7qDGCsyzJwohVaoX"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4uiMn2g0pgTrhN096QJhbp"
            },
            "href": "https://api.spotify.com/v1/artists/4uiMn2g0pgTrhN096QJhbp",
            "id": "4uiMn2g0pgTrhN096QJhbp",
            "name": "Borgeous",
            "type": "artist",
            "uri": "spotify:artist:4uiMn2g0pgTrhN096QJhbp"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1QdG3nKKTrNWlN9x9t1cH6"
        },
        "name": "FRIENDS - Borgeous Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "My Life"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/28j8lBWDdDSHSSt5oPlsX2"
            },
            "href": "https://api.spotify.com/v1/artists/28j8lBWDdDSHSSt5oPlsX2",
            "id": "28j8lBWDdDSHSSt5oPlsX2",
            "name": "ZHU",
            "type": "artist",
            "uri": "spotify:artist:28j8lBWDdDSHSSt5oPlsX2"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5INjqkS1o8h1imAzPqGZBb"
            },
            "href": "https://api.spotify.com/v1/artists/5INjqkS1o8h1imAzPqGZBb",
            "id": "5INjqkS1o8h1imAzPqGZBb",
            "name": "Tame Impala",
            "type": "artist",
            "uri": "spotify:artist:5INjqkS1o8h1imAzPqGZBb"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2NDZ6i6UfOUSKgFiTQKbnv"
        },
        "name": "My Life"
      }
    },
    {
      "track": {
        "album": {
          "name": "AVICI (01)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
            },
            "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
            "id": "1vCWHaC5f2uS3yhpwWbIA6",
            "name": "Avicii",
            "type": "artist",
            "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5gw5ANPCVcxU0maLiGRzzP"
            },
            "href": "https://api.spotify.com/v1/artists/5gw5ANPCVcxU0maLiGRzzP",
            "id": "5gw5ANPCVcxU0maLiGRzzP",
            "name": "Billy Raffoul",
            "type": "artist",
            "uri": "spotify:artist:5gw5ANPCVcxU0maLiGRzzP"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/630svau24EHHzw1kNk0Bdq"
        },
        "name": "You Be Love (feat. Billy Raffoul)"
      }
    },
    {
      "track": {
        "album": {
          "name": "HUMAN"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4FqPRilb0Ja0TKG3RS3y4s"
            },
            "href": "https://api.spotify.com/v1/artists/4FqPRilb0Ja0TKG3RS3y4s",
            "id": "4FqPRilb0Ja0TKG3RS3y4s",
            "name": "Steve Angello",
            "type": "artist",
            "uri": "spotify:artist:4FqPRilb0Ja0TKG3RS3y4s"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/66AE89GQTx88zLYhXn1wFK"
            },
            "href": "https://api.spotify.com/v1/artists/66AE89GQTx88zLYhXn1wFK",
            "id": "66AE89GQTx88zLYhXn1wFK",
            "name": "Sam Martin",
            "type": "artist",
            "uri": "spotify:artist:66AE89GQTx88zLYhXn1wFK"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6xeCQCtG0VVzV69qTiUg21"
        },
        "name": "Nothing Scares Me Anymore"
      }
    },
    {
      "track": {
        "album": {
          "name": "Happy Now"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2qxJFvFYMEDqd7ui6kSAcq"
            },
            "href": "https://api.spotify.com/v1/artists/2qxJFvFYMEDqd7ui6kSAcq",
            "id": "2qxJFvFYMEDqd7ui6kSAcq",
            "name": "Zedd",
            "type": "artist",
            "uri": "spotify:artist:2qxJFvFYMEDqd7ui6kSAcq"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/67MNhiAICFY6Pwc2YxCO0K"
            },
            "href": "https://api.spotify.com/v1/artists/67MNhiAICFY6Pwc2YxCO0K",
            "id": "67MNhiAICFY6Pwc2YxCO0K",
            "name": "Elley Duhé",
            "type": "artist",
            "uri": "spotify:artist:67MNhiAICFY6Pwc2YxCO0K"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4keoy2fqgwGnbWlm3ZVZFa"
        },
        "name": "Happy Now"
      }
    },
    {
      "track": {
        "album": {
          "name": "Fun"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6TQj5BFPooTa08A7pk8AQ1"
            },
            "href": "https://api.spotify.com/v1/artists/6TQj5BFPooTa08A7pk8AQ1",
            "id": "6TQj5BFPooTa08A7pk8AQ1",
            "name": "Kaskade",
            "type": "artist",
            "uri": "spotify:artist:6TQj5BFPooTa08A7pk8AQ1"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3IHsD0sttucHrX8b32Vcab"
            },
            "href": "https://api.spotify.com/v1/artists/3IHsD0sttucHrX8b32Vcab",
            "id": "3IHsD0sttucHrX8b32Vcab",
            "name": "BROHUG",
            "type": "artist",
            "uri": "spotify:artist:3IHsD0sttucHrX8b32Vcab"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7ladzyDVpwhv848vat5v9P"
            },
            "href": "https://api.spotify.com/v1/artists/7ladzyDVpwhv848vat5v9P",
            "id": "7ladzyDVpwhv848vat5v9P",
            "name": "Mr. Tape",
            "type": "artist",
            "uri": "spotify:artist:7ladzyDVpwhv848vat5v9P"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2StukZYqvy5IZmVestMrWo"
            },
            "href": "https://api.spotify.com/v1/artists/2StukZYqvy5IZmVestMrWo",
            "id": "2StukZYqvy5IZmVestMrWo",
            "name": "Madge",
            "type": "artist",
            "uri": "spotify:artist:2StukZYqvy5IZmVestMrWo"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6quwZWSOygVjpaTG84whzq"
        },
        "name": "Fun"
      }
    },
    {
      "track": {
        "album": {
          "name": "Spaceship (feat. Uffie)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4sTQVOfp9vEMCemLw50sbu"
            },
            "href": "https://api.spotify.com/v1/artists/4sTQVOfp9vEMCemLw50sbu",
            "id": "4sTQVOfp9vEMCemLw50sbu",
            "name": "Galantis",
            "type": "artist",
            "uri": "spotify:artist:4sTQVOfp9vEMCemLw50sbu"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2s6lxOYvvCvzpHtd3VyuMj"
            },
            "href": "https://api.spotify.com/v1/artists/2s6lxOYvvCvzpHtd3VyuMj",
            "id": "2s6lxOYvvCvzpHtd3VyuMj",
            "name": "Uffie",
            "type": "artist",
            "uri": "spotify:artist:2s6lxOYvvCvzpHtd3VyuMj"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2aOlxywgl4nCD4Xh2mLWM7"
        },
        "name": "Spaceship (feat. Uffie)"
      }
    },
    {
      "track": {
        "album": {
          "name": "Solo (feat. Demi Lovato)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6MDME20pz9RveH9rEXvrOM"
            },
            "href": "https://api.spotify.com/v1/artists/6MDME20pz9RveH9rEXvrOM",
            "id": "6MDME20pz9RveH9rEXvrOM",
            "name": "Clean Bandit",
            "type": "artist",
            "uri": "spotify:artist:6MDME20pz9RveH9rEXvrOM"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6S2OmqARrzebs0tKUEyXyp"
            },
            "href": "https://api.spotify.com/v1/artists/6S2OmqARrzebs0tKUEyXyp",
            "id": "6S2OmqARrzebs0tKUEyXyp",
            "name": "Demi Lovato",
            "type": "artist",
            "uri": "spotify:artist:6S2OmqARrzebs0tKUEyXyp"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6kPJZM97LwdG9QIsT7khp6"
        },
        "name": "Solo (feat. Demi Lovato)"
      }
    },
    {
      "track": {
        "album": {
          "name": "Common Ground"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/10gzBoINW3cLJfZUka8Zoe"
            },
            "href": "https://api.spotify.com/v1/artists/10gzBoINW3cLJfZUka8Zoe",
            "id": "10gzBoINW3cLJfZUka8Zoe",
            "name": "Above & Beyond",
            "type": "artist",
            "uri": "spotify:artist:10gzBoINW3cLJfZUka8Zoe"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5JbD3IL6449LrMT8ct6KTB"
            },
            "href": "https://api.spotify.com/v1/artists/5JbD3IL6449LrMT8ct6KTB",
            "id": "5JbD3IL6449LrMT8ct6KTB",
            "name": "Richard Bedford",
            "type": "artist",
            "uri": "spotify:artist:5JbD3IL6449LrMT8ct6KTB"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6poaggkSYGIoUjyuippcQ2"
        },
        "name": "Northern Soul"
      }
    },
    {
      "track": {
        "album": {
          "name": "Kids in Love"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/23fqKkggKUBHNkbKtXEls4"
            },
            "href": "https://api.spotify.com/v1/artists/23fqKkggKUBHNkbKtXEls4",
            "id": "23fqKkggKUBHNkbKtXEls4",
            "name": "Kygo",
            "type": "artist",
            "uri": "spotify:artist:23fqKkggKUBHNkbKtXEls4"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/360IAlyVv4PCEVjgyMZrxK"
            },
            "href": "https://api.spotify.com/v1/artists/360IAlyVv4PCEVjgyMZrxK",
            "id": "360IAlyVv4PCEVjgyMZrxK",
            "name": "Miguel",
            "type": "artist",
            "uri": "spotify:artist:360IAlyVv4PCEVjgyMZrxK"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6xTU6B6nFwKKTSZ9ySXS80"
        },
        "name": "Remind Me to Forget"
      }
    },
    {
      "track": {
        "album": {
          "name": "Ocean"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6fcTRFpz0yH79qSKfof7lp"
            },
            "href": "https://api.spotify.com/v1/artists/6fcTRFpz0yH79qSKfof7lp",
            "id": "6fcTRFpz0yH79qSKfof7lp",
            "name": "Seven Lions",
            "type": "artist",
            "uri": "spotify:artist:6fcTRFpz0yH79qSKfof7lp"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6CCTvLyIHqUhY6VQizt150"
            },
            "href": "https://api.spotify.com/v1/artists/6CCTvLyIHqUhY6VQizt150",
            "id": "6CCTvLyIHqUhY6VQizt150",
            "name": "Jason Ross",
            "type": "artist",
            "uri": "spotify:artist:6CCTvLyIHqUhY6VQizt150"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5d1oOpLkM76Tgr2zWMTYkm"
            },
            "href": "https://api.spotify.com/v1/artists/5d1oOpLkM76Tgr2zWMTYkm",
            "id": "5d1oOpLkM76Tgr2zWMTYkm",
            "name": "Jonathan Mendelsohn",
            "type": "artist",
            "uri": "spotify:artist:5d1oOpLkM76Tgr2zWMTYkm"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5ZQMiwA8y8BEslhMmtLxLv"
        },
        "name": "Ocean"
      }
    },
    {
      "track": {
        "album": {
          "name": "X's"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/78DWNk8gFHU30TGITAgbM7"
            },
            "href": "https://api.spotify.com/v1/artists/78DWNk8gFHU30TGITAgbM7",
            "id": "78DWNk8gFHU30TGITAgbM7",
            "name": "CMC$",
            "type": "artist",
            "uri": "spotify:artist:78DWNk8gFHU30TGITAgbM7"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2xgAJkalFHfceCNGETOkyM"
            },
            "href": "https://api.spotify.com/v1/artists/2xgAJkalFHfceCNGETOkyM",
            "id": "2xgAJkalFHfceCNGETOkyM",
            "name": "Grx",
            "type": "artist",
            "uri": "spotify:artist:2xgAJkalFHfceCNGETOkyM"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1VBflYyxBhnDc9uVib98rw"
            },
            "href": "https://api.spotify.com/v1/artists/1VBflYyxBhnDc9uVib98rw",
            "id": "1VBflYyxBhnDc9uVib98rw",
            "name": "Icona Pop",
            "type": "artist",
            "uri": "spotify:artist:1VBflYyxBhnDc9uVib98rw"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3oW1QkDNYPLoM3alqUVXkY"
        },
        "name": "X's"
      }
    },
    {
      "track": {
        "album": {
          "name": "Sick Boy...Side Effects"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp"
            },
            "href": "https://api.spotify.com/v1/artists/69GGBxA162lTqCwzJG5jLp",
            "id": "69GGBxA162lTqCwzJG5jLp",
            "name": "The Chainsmokers",
            "type": "artist",
            "uri": "spotify:artist:69GGBxA162lTqCwzJG5jLp"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/76yeOnINtQSXyoEHbkYmtY"
            },
            "href": "https://api.spotify.com/v1/artists/76yeOnINtQSXyoEHbkYmtY",
            "id": "76yeOnINtQSXyoEHbkYmtY",
            "name": "Drew Love",
            "type": "artist",
            "uri": "spotify:artist:76yeOnINtQSXyoEHbkYmtY"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6mWDwN58PgiPiDXkfSfB4J"
        },
        "name": "Somebody"
      }
    },
    {
      "track": {
        "album": {
          "name": "Ignite (feat. SEUNGRI)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6pWcSL9wSJZQ9ne0TnhdWr"
            },
            "href": "https://api.spotify.com/v1/artists/6pWcSL9wSJZQ9ne0TnhdWr",
            "id": "6pWcSL9wSJZQ9ne0TnhdWr",
            "name": "K-391",
            "type": "artist",
            "uri": "spotify:artist:6pWcSL9wSJZQ9ne0TnhdWr"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7vk5e3vY1uw9plTHJAMwjN"
            },
            "href": "https://api.spotify.com/v1/artists/7vk5e3vY1uw9plTHJAMwjN",
            "id": "7vk5e3vY1uw9plTHJAMwjN",
            "name": "Alan Walker",
            "type": "artist",
            "uri": "spotify:artist:7vk5e3vY1uw9plTHJAMwjN"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2Tg0aF5cbZktYFzgR1iAKv"
            },
            "href": "https://api.spotify.com/v1/artists/2Tg0aF5cbZktYFzgR1iAKv",
            "id": "2Tg0aF5cbZktYFzgR1iAKv",
            "name": "Julie Bergan",
            "type": "artist",
            "uri": "spotify:artist:2Tg0aF5cbZktYFzgR1iAKv"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/20j1uz7iDOtIvIzCr5S8nx"
            },
            "href": "https://api.spotify.com/v1/artists/20j1uz7iDOtIvIzCr5S8nx",
            "id": "20j1uz7iDOtIvIzCr5S8nx",
            "name": "SEUNGRI",
            "type": "artist",
            "uri": "spotify:artist:20j1uz7iDOtIvIzCr5S8nx"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0UMLejbZXf7YVgnfxURvVr"
        },
        "name": "Ignite (feat. SEUNGRI)"
      }
    },
    {
      "track": {
        "album": {
          "name": "AVICI (01)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6"
            },
            "href": "https://api.spotify.com/v1/artists/1vCWHaC5f2uS3yhpwWbIA6",
            "id": "1vCWHaC5f2uS3yhpwWbIA6",
            "name": "Avicii",
            "type": "artist",
            "uri": "spotify:artist:1vCWHaC5f2uS3yhpwWbIA6"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5CCwRZC6euC8Odo6y9X8jr"
            },
            "href": "https://api.spotify.com/v1/artists/5CCwRZC6euC8Odo6y9X8jr",
            "id": "5CCwRZC6euC8Odo6y9X8jr",
            "name": "Rita Ora",
            "type": "artist",
            "uri": "spotify:artist:5CCwRZC6euC8Odo6y9X8jr"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/75NhhYjHO43mvZgYtnXgti"
        },
        "name": "Lonely Together (feat. Rita Ora)"
      }
    },
    {
      "track": {
        "album": {
          "name": "Footprint"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4xSQ9zt3zGyyiCXazv4mhf"
            },
            "href": "https://api.spotify.com/v1/artists/4xSQ9zt3zGyyiCXazv4mhf",
            "id": "4xSQ9zt3zGyyiCXazv4mhf",
            "name": "Steve Brian",
            "type": "artist",
            "uri": "spotify:artist:4xSQ9zt3zGyyiCXazv4mhf"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6sczuMreL6JAF18pqPp4YT"
        },
        "name": "Footprint"
      }
    },
    {
      "track": {
        "album": {
          "name": "Lest We Forget"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5GehdPjguGOCZifnKNrXi9"
            },
            "href": "https://api.spotify.com/v1/artists/5GehdPjguGOCZifnKNrXi9",
            "id": "5GehdPjguGOCZifnKNrXi9",
            "name": "Tim Mason",
            "type": "artist",
            "uri": "spotify:artist:5GehdPjguGOCZifnKNrXi9"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3EnUkQ9iGHXHQI9gujiZkF"
        },
        "name": "Lest We Forget"
      }
    },
    {
      "track": {
        "album": {
          "name": "I Love It"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7DMveApC7UnC2NPfPvlHSU"
            },
            "href": "https://api.spotify.com/v1/artists/7DMveApC7UnC2NPfPvlHSU",
            "id": "7DMveApC7UnC2NPfPvlHSU",
            "name": "Cheat Codes",
            "type": "artist",
            "uri": "spotify:artist:7DMveApC7UnC2NPfPvlHSU"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5X4LWwbUFNzPkEas04uU82"
            },
            "href": "https://api.spotify.com/v1/artists/5X4LWwbUFNzPkEas04uU82",
            "id": "5X4LWwbUFNzPkEas04uU82",
            "name": "DVBBS",
            "type": "artist",
            "uri": "spotify:artist:5X4LWwbUFNzPkEas04uU82"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/66poU6LBLnYZmftAYXMbDH"
        },
        "name": "I Love It"
      }
    },
    {
      "track": {
        "album": {
          "name": "Better Not (Remixes)"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7wg1qvie3KqDNQbAkTdbX0"
            },
            "href": "https://api.spotify.com/v1/artists/7wg1qvie3KqDNQbAkTdbX0",
            "id": "7wg1qvie3KqDNQbAkTdbX0",
            "name": "Louis The Child",
            "type": "artist",
            "uri": "spotify:artist:7wg1qvie3KqDNQbAkTdbX0"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0FL2d6iFFNAV3yBUbXjZ1U"
            },
            "href": "https://api.spotify.com/v1/artists/0FL2d6iFFNAV3yBUbXjZ1U",
            "id": "0FL2d6iFFNAV3yBUbXjZ1U",
            "name": "Wafia",
            "type": "artist",
            "uri": "spotify:artist:0FL2d6iFFNAV3yBUbXjZ1U"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0BBwlSQvHHtahgYpLj1wJE"
            },
            "href": "https://api.spotify.com/v1/artists/0BBwlSQvHHtahgYpLj1wJE",
            "id": "0BBwlSQvHHtahgYpLj1wJE",
            "name": "Shaun Frank",
            "type": "artist",
            "uri": "spotify:artist:0BBwlSQvHHtahgYpLj1wJE"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7kGIyYQc44EQcJR3HH314y"
        },
        "name": "Better Not (feat. Wafia) - Shaun Frank Remix"
      }
    },
    {
      "track": {
        "album": {
          "name": "Higher"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4xnMDfgEmXZEEDdITKcGuE"
            },
            "href": "https://api.spotify.com/v1/artists/4xnMDfgEmXZEEDdITKcGuE",
            "id": "4xnMDfgEmXZEEDdITKcGuE",
            "name": "Audien",
            "type": "artist",
            "uri": "spotify:artist:4xnMDfgEmXZEEDdITKcGuE"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/68Fx3kHvTjMLGwcBzr5X7U"
            },
            "href": "https://api.spotify.com/v1/artists/68Fx3kHvTjMLGwcBzr5X7U",
            "id": "68Fx3kHvTjMLGwcBzr5X7U",
            "name": "Cecilia Gault",
            "type": "artist",
            "uri": "spotify:artist:68Fx3kHvTjMLGwcBzr5X7U"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/61h6ZJSXHwElzSXv2WDtmL"
        },
        "name": "Higher"
      }
    },
    {
      "track": {
        "album": {
          "name": "mau5ville: Level 1"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2CIMQHirSU0MQqyYHq0eOx"
            },
            "href": "https://api.spotify.com/v1/artists/2CIMQHirSU0MQqyYHq0eOx",
            "id": "2CIMQHirSU0MQqyYHq0eOx",
            "name": "deadmau5",
            "type": "artist",
            "uri": "spotify:artist:2CIMQHirSU0MQqyYHq0eOx"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2SNg8nqwOHF1eZgRnL9zes"
            },
            "href": "https://api.spotify.com/v1/artists/2SNg8nqwOHF1eZgRnL9zes",
            "id": "2SNg8nqwOHF1eZgRnL9zes",
            "name": "Rob Swire",
            "type": "artist",
            "uri": "spotify:artist:2SNg8nqwOHF1eZgRnL9zes"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2nLgWMdYPO35GGpwX2xo23"
        },
        "name": "Monophobia"
      }
    },
    {
      "track": {
        "album": {
          "name": "Anywhere"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/01pKrlgPJhm5dB4lneYAqS"
            },
            "href": "https://api.spotify.com/v1/artists/01pKrlgPJhm5dB4lneYAqS",
            "id": "01pKrlgPJhm5dB4lneYAqS",
            "name": "Sigma",
            "type": "artist",
            "uri": "spotify:artist:01pKrlgPJhm5dB4lneYAqS"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6lD9nDl7jBUSIPDMAMZjuD"
        },
        "name": "Anywhere"
      }
    },
    {
      "track": {
        "album": {
          "name": "Lick It"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0deIjoDjl9g9Zpw0sCIOHh"
            },
            "href": "https://api.spotify.com/v1/artists/0deIjoDjl9g9Zpw0sCIOHh",
            "id": "0deIjoDjl9g9Zpw0sCIOHh",
            "name": "Valentino Khan",
            "type": "artist",
            "uri": "spotify:artist:0deIjoDjl9g9Zpw0sCIOHh"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2AUHVjR5lhg6GcztbGvRkc"
        },
        "name": "Lick It"
      }
    },
    {
      "track": {
        "album": {
          "name": "Wake Me When It's Quiet"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0gNDtB2LFXVzalP35MXaql"
            },
            "href": "https://api.spotify.com/v1/artists/0gNDtB2LFXVzalP35MXaql",
            "id": "0gNDtB2LFXVzalP35MXaql",
            "name": "Hilda",
            "type": "artist",
            "uri": "spotify:artist:0gNDtB2LFXVzalP35MXaql"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1l2ekx5skC4gJH8djERwh1"
            },
            "href": "https://api.spotify.com/v1/artists/1l2ekx5skC4gJH8djERwh1",
            "id": "1l2ekx5skC4gJH8djERwh1",
            "name": "Don Diablo",
            "type": "artist",
            "uri": "spotify:artist:1l2ekx5skC4gJH8djERwh1"
          }
        ],
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5JCZ1e1ahbCkzwX62BbsY7"
        },
        "name": "Wake Me When It's Quiet"
      }
    }
  ]
}'''.encode("utf-8")

for track in json.loads(pop)['items']:
    print u"{}|{}|{}|{}".format(track['track']['name'], track['track']['artists'][0]['name'], track['track']['album']['name'], track['track']['external_urls'])
