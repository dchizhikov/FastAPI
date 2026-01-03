start_server()
base_url = output.eval_js(f"google.colab.kernel.proxyPort({port_g})")
print(f"Доступ к приложению по адресу: {base_url}")

#stop_server()
