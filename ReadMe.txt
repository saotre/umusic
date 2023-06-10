1. Запрос на создание пользователя:
   пример:
   request:
      POST http://localhost:8000/user
      body: {"name": "Egor Andreev"}
   response:
      {
         "name": "Egor Andreev",
         "id": "9d9102ca-25bb-4199-abc4-72a6c5db1fc6",
         "token": "2b8f40d5-7073-4591-8ee0-46444fff1ded",
         "created_at": "2023-06-06T16:51:50.603229"
      }

2. Запрос добавление аудиозаписи
   пример:
   request:
      POST http://localhost:8000/audio?user_id=9d9102ca-25bb-4199-abc4-72a6c5db1fc6&token=2b8f40d5-7073-4591-8ee0-46444fff1ded
      body: File: file_example_WAV_1MG.wav (type: "audio/wav"; size: 1073218 bytes)
   response:
      "http://localhost:8000/record?id=36d18862-4a6c-4c68-82e2-ae3d9fd46a38&user=9d9102ca-25bb-4199-abc4-72a6c5db1fc6"

3. Запрос на скачивание аудиозаписи.
   пример:
   request:
      GET  http://localhost:8000/record?id=36d18862-4a6c-4c68-82e2-ae3d9fd46a38&user=9d9102ca-25bb-4199-abc4-72a6c5db1fc6
   response:
      файл mp3: 36d18862-4a6c-4c68-82e2-ae3d9fd46a38.mp3 (имя файла: id_аудиозаписи.mp3)


