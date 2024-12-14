"""
github.com/evilstrix
"""

try:
    import pystyle
    import os
    import typing
    import tls_client
    import string
    import random
    import colorama
    import concurrent.futures
    from concurrent.futures import ThreadPoolExecutor, as_completed
except ImportError:
    os.system('pip install pystyle')
    os.system('pip install colorama')
    os.system('pip install typing')

from pystyle import(
    Colors, Colorate, System, Center
)

from colorama import Fore
from tls_client import Session

from typing import(
    List, Dict, Optional, Union, Any, Callable, TypeVar, Tuple
) 

class UI:
    def ask(question: str) -> str:
        return input(
            (Colorate.Horizontal(Colors.blue_to_white, question))
        )
    
class logging:
    @staticmethod
    def failure(message: str) -> None:
        print(Colorate.Horizontal(Colors.red_to_white, message))

    @staticmethod
    def succes(message: str) -> None:
        print(Colorate.Horizontal(Colors.green_to_white, message))

    @staticmethod
    def warning(message: str) -> None:
        print(Colorate.Horizontal(Colors.red_to_yellow, message))

log = logging()

class Colorss: 
    colors = [
      f'\033[34m',  
      f'\033[92m',  
      f'\033[91m',  
      f'\033[31m',  
    ]

banner: str = f"""
   {Colorss.colors[1]}______                          _____                                          
  / ____/________  __  ______     / ___/____  ____ _____ ___  ____ ___  ___  _____
{Colorss.colors[3]} / / __/ ___/ __ \/ / / / __ \    \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
/ /_/ / /  / /_/ / /_/ / /_/ /   ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /    
{Colorss.colors[1]}\____/_/   \____/\__,_/ .___/   /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
                     {Colorss.colors[2]}/_/            /_/                                               
                                                              
"""

class Utils:
   """ Good Covering """
   def clear() -> None:
      return(
         os.system('clear||cls') 
      ) 
   
   def title(title: str) -> str:
      return(
         os.system(f'title {title}')
      )

class Functions:
    @staticmethod
    def get_session(token: str) -> tls_client.Session:
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "authorization": token,
            "cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==",
            "referer": "https://discord.com/channels/967617613960187974/981260247807168532",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllYW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        }

        session = tls_client.Session()
        session.headers = headers
        return session

    @staticmethod
    def friends(session: tls_client.Session) -> List[Dict[str, Union[str, int]]]:
        response = session.get('https://discord.com/api/v10/users/@me/relationships')
        
        if response.status_code == 200:
            return response.json()
        else:
            return []

    @staticmethod
    def spam(session: tls_client.Session, user_id: str, victim: str, group_name: str) -> Union[str, None]:
        url = 'https://discord.com/api/v10/users/@me/channels'
        payload = {
            'recipients': [victim, user_id],
            'type': 1
        }
        response = session.post(url, json=payload)
        
        if response.status_code == 200:
            channel_id = response.json()['id']
            
            update_payload = {
                'name': group_name
            }
            update_response = session.patch(f'https://discord.com/api/v10/channels/{channel_id}', json=update_payload)
            
            if update_response.status_code == 200:
                return channel_id
            else:
                log.good("Failed to upd gc name")
                return None
        else:
            print(f"Error [{response.status_code}] - {response.text}")
            return None

    @staticmethod
    def send_message(session: tls_client.Session, channel_id: str, message: str) -> bool:
        message_url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
        payload = {
            'content': message
        }
        response = session.post(message_url, json=payload)
        
        if response.status_code == 200:
            log.good("Succesfully sent msg")
            return True
        else:
            log.good("Failed sending msg")
            return False

    @staticmethod
    def spammsg(session: tls_client.Session, user_id: str, victim: str, group_name: str, message: str) -> Union[str, None]:
        group_id = Functions.spam(session, user_id, victim, group_name)
        
        if group_id:
            log.succes(f"Succesfully created group with {group_id}")
            
            if message:
                Functions.send_message(session, group_id, message)
            return True
        else:
            log.failure(f"Failed to create group")
            return False

    @staticmethod
    def gcspam():
        token: str = UI.ask("Token: ")
        user_id: str = UI.ask("Your id: ")
        victim: str = UI.ask("Victim: ").strip()
        
        group_name: str = UI.ask("Group Name: ").strip()

        spam_choice: str = UI.ask("Msg mode? (y/n): ").strip().lower()
        message: str = ""

        if spam_choice == 'y':
            message = UI.ask("Message: ").strip()

        num_groups: int = int(UI.ask("How many groups?: "))
        thread_count: int = int(UI.ask("Thread Count: "))

        if not victim or not group_name:
            log.warning("Victim or group name cannot be empty")
            return

        session = Functions.get_session(token)

        Utils.clear()
        print(banner)

        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            futures = []
            
            for i in range(num_groups):
                group_name_with_index = f"{group_name}_{i+1}"
                futures.append(executor.submit(Functions.spammsg, session, user_id, victim, group_name_with_index, message))
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    log.succes("Succesfully created group")
                else:
                    log.failure("Failed creating group")


def main() -> str:
    Utils.clear()
    print(banner)
     
    choice = UI.ask('Enter "Y" To start the gc spammer')

    options = {
      'y': Functions.gcspam,
    }

    if choice in options:
        options[choice]()  
    else:
        main()

if __name__ == "__main__":
    main()
