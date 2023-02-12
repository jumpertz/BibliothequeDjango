# BibliothequeDjango

## 🖥️ How to start the project?

1. Clone the project
2. Run `make build` in order to download and build the latest version of the images
3. Run `make run` to start the project. You can add the option `-d` to run it in background

## 🗃️ Database migrations

In order to make a migration after adding a new entity, you can use the following command:

```bash
make migrations
```

```bash
make migrate
```

You can generate a superuser for the admin part

```bash
make generate-superuser
```

All the commands are in the Makefile