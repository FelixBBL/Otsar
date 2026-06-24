// Otsar desktop shell.
// Hides the console window on Windows release builds.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::Manager;

fn main() {
    tauri::Builder::default()
        // Registered now so the future "open BHSA folder" feature
        // (native folder picker + .tf reading) needs no Rust changes.
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_fs::init())
        .setup(|app| {
            // High-res window icon so the running taskbar button is crisp at any DPI.
            if let Some(win) = app.get_webview_window("main") {
                let icon = tauri::image::Image::new(include_bytes!("../icons/icon_rgba.bin"), 256, 256);
                let _ = win.set_icon(icon);
            }
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running Otsar");
}
