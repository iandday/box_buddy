# Usage

## Generate Testing Data

Testing data can be generated to demo the application's functionality before entering real data.  Run the command below from the application's container to generate data

```bash
uv run manage.py generate_fake_data
```

The testing data can be removed without effecting any other data with the command below.

```bash
uv run manage.py delete_fake_data
```
