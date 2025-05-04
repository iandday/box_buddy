# Dewvelopment

## Service URLS

* Traefik Portal: [https://traefik.localhost](https://traefik.localhost)
* Mailpit Interface: [https://mail.localhost](https://mail.localhost)
* Flower Admin: [https://flower.localhost](https://flower.localhost)
* App: [https://localhost](https://localhost)

## Generate Fake Data for Testing

The custom Django command will create the following objects and the appropriate links to populate the database for development or testing.  The command can be run multiple times which will generate new objects with the exception of `Location` objects.

* 4 Locations
* 10 Boxes
* 20 Items
* 10 Files
* 10 URLs

```bash
uv run manage.py generate_fake_data
```

## Delete Fake Data

The custom Django command will delete all objects created by the `generate_fake_data` command

```bash
uv run manage.py delete_fake_data
```


https://github.com/dobicinaitis/tailwind-cli-extra
