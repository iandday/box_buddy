# Dewvelopment

## Service URLS

* App: [https://localhost](https://localhost)
* Traefik Portal: [https://traefik.localhost](https://traefik.localhost)
* Mailpit Interface: [https://mail.localhost](https://mail.localhost)
* Flower Admin: [https://flower.localhost](https://flower.localhost)
* Local Documentation: [http://localhost:8001/](http://localhost:8001/)

## Generate Fake Data for Testing

The custom Django command will create the following objects and the appropriate links to populate the database for development or testing.

```bash
uv run manage.py generate_fake_data
```

## Delete Fake Data

The custom Django command will delete all objects created by the `generate_fake_data` command

```bash
uv run manage.py delete_fake_data
```
