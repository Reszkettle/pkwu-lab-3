# pkwu-lab-3

# Routes

You'll find here the routes exposed by this repository. Note that you can also review them through the interactive API docs. The interactive API docs are located at `/docs` and `/redoc`

## String router

### **Analyse string**

#### POST `/analyse-string`

#### **Description**:

Uses an external api for analyzing the string.
Link to the documentation: [analyse string docs](https://github.com/Reszkettle/pkwu-lab-2#readme)

Additionally, it allows to select the return format.

#### **Request Body**

| Type     | Name      | Optional | Description                                          |
| -------- | --------- | -------- | ---------------------------------------------------- |
| `string` | string    | No       | string that will be analyzed                         |
| `string` | substring | Yes      | optional substring which occurrences will be counted |
| `string` | format    | No       | one of the following values: ( json / xml / csv )    |

### Response

On success (HTTP 200 status) this endpoint returns single string that contains the structure for the format that you've provided in request body:

Example for Request Body:

```json
{
	"string": "Nieborak1#",
	"substring": "rak",
	"format": "..."
}
```

### Response string when `format` is:

- json
  ```json
  {
  	"lower_case_letters_count": 7,
  	"upper_case_letters_count": 1,
  	"digits_count": 1,
  	"special_characters_count": 1,
  	"substring_occurrences_count": 1
  }
  ```
- xml
  ```xml
  <?xml version=\"1.0\" encoding=\"UTF-8\" ?>
  <string-analyze-statistics>
    <lower_case_letters_count>7</lower_case_letters_count>
    <upper_case_letters_count>1</upper_case_letters_count>
    <digits_count>1</digits_count>
    <special_characters_count>1</special_characters_count>
    <substring_occurrences_count>1</substring_occurrences_count>
  </string-analyze-statistics>
  ```
- csv
  ```csv
  lower_case_letters_count,upper_case_letters_count,digits_count,special_characters_count,substring_occurrences_count
  7,1,1,1,1
  ```
