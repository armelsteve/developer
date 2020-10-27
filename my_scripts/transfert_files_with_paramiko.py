import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="armelCentos.int.kronos.com",username="armel",password="Pass123!")
sftp_client = ssh.open_sftp()

#sftp_client.get("/home/armel/file_test.txt","/Users/armel.gansop/script/developer/my_scripts/file_test.txt")
sftp_client.put("/Users/armel.gansop/script/developer/my_scripts/text.json","/home/armel/text.json")
sftp_client.close()
ssh.close()
