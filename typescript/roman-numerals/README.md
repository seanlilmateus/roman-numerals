# Arabic to roman number converter

## Requirements

- [Node >=16](https://nodejs.org/en/)

*Optional:*
- [NVM](https://github.com/nvm-sh/nvm) for easier version switching
- [mob](https://mob.sh/) for timekeeping and easier code handover

## SetUp

```bash
npm install
npm run test && npm run test:e2e
```

## User story

As a researcher I want to have a function,
with which I can convert any arabic number to its corresponding roman
number so that I can confirm my years for important historical events

## Test cases

| Arabic number | roman number |
|---------------|--------------|
| 1             | I            |
| 2             | II           |
| 3             | III          |
| 4             | IV           |
| 5             | V            |
| 6             | VI           |
| 7             | VII          |
| 8             | VIII         |
| 9             | IX           |
| 10            | X            |
| 11            | XI           |
| 14            | XIV          |
| 15            | XV           |
| 17            | XVII         |
| 19            | XIX          |
| 20            | XX           |
| 34            | XXXIV        |
| 39            | XXXIX        |
| 40            | XL           |
| 45            | XLV          |
| 50            | L            |
| 100           | C            |
| 400           | CD           |
| 500           | D            |
| 900           | CM           |
| 1000          | M            |


## Running Tests

```bash
# unit tests
npm test
```