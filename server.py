import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/SportspageFeeds/api/sportspage-feeds'

mcp = FastMCP('sportspage-feeds')

@mcp.tool()
def rankings(league: Annotated[str, Field(description='')]) -> dict: 
    '''League rankings (currently supports NCAAF and NCAAB)'''
    url = 'https://sportspage-feeds.p.rapidapi.com/rankings'
    headers = {'x-rapidapi-host': 'sportspage-feeds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams(league: Annotated[str, Field(description='A valid league code (i.e., NFL, NBA, MLB, NHL, NCAAF, or NCAAB)')],
          division: Annotated[Union[str, None], Field(description='A division within the specified conference')] = None,
          conference: Annotated[Union[str, None], Field(description='A conference within the specified league')] = None) -> dict: 
    '''Returns a list of teams within a specified league, conference, or division.'''
    url = 'https://sportspage-feeds.p.rapidapi.com/teams'
    headers = {'x-rapidapi-host': 'sportspage-feeds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'division': division,
        'conference': conference,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def game_by_id(gameId: Annotated[str, Field(description='A unique game identifier')]) -> dict: 
    '''Returns a specific game based on its ID.'''
    url = 'https://sportspage-feeds.p.rapidapi.com/gameById'
    headers = {'x-rapidapi-host': 'sportspage-feeds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameId': gameId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def games(odds: Annotated[Union[str, None], Field(description='A comma-separated filter to select games with one or more of the following odds types: \\\\\\"spread\\\\\\", \\\\\\"moneyline\\\\\\", \\\\\\"total\\\\\\", or \\\\\\"any\\\\\\"')] = None,
          status: Annotated[Union[str, None], Field(description='A valid status of one of the following: \\\\\\"scheduled\\\\\\", \\\\\\"in progress\\\\\\", \\\\\\"final\\\\\\", \\\\\\"canceled\\\\\\", or \\\\\\"delayed\\\\\\"')] = None,
          league: Annotated[Union[str, None], Field(description='A valid league code (i.e., NFL, NBA, MLB, NHL, NCAAF, or NCAAB)')] = None,
          skip: Annotated[Union[str, None], Field(description='The number of game results to skip, which is required to access results beyond the first 100')] = None,
          conference: Annotated[Union[str, None], Field(description='A conference within the specified league')] = None,
          date: Annotated[Union[str, None], Field(description='One or two (comma-separated) YYYY-MM-DD- or ISO-formatted dates')] = None,
          team: Annotated[Union[str, None], Field(description='A team participating in one or more games')] = None,
          division: Annotated[Union[str, None], Field(description='A division within the specified conference')] = None) -> dict: 
    '''Returns a list of games.'''
    url = 'https://sportspage-feeds.p.rapidapi.com/games'
    headers = {'x-rapidapi-host': 'sportspage-feeds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'odds': odds,
        'status': status,
        'league': league,
        'skip': skip,
        'conference': conference,
        'date': date,
        'team': team,
        'division': division,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def conferences(league: Annotated[str, Field(description='A valid league code (i.e., NFL, NBA, MLB, NHL, NCAAF, or NCAAB)')]) -> dict: 
    '''Returns a list of conferences and divisions within the specified league. Use this endpoint to obtain conference and division names to be used as parameters for other requests.'''
    url = 'https://sportspage-feeds.p.rapidapi.com/conferences'
    headers = {'x-rapidapi-host': 'sportspage-feeds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def odds(gameId: Annotated[str, Field(description='A unique game identifier')],
         type: Annotated[Union[str, None], Field(description='An odds type of one of the following: \\"spread\\", \\"moneyline\\", \\"total\\", or \\"any\\"')] = None) -> dict: 
    '''Returns the odds history for a game by type.'''
    url = 'https://sportspage-feeds.p.rapidapi.com/odds'
    headers = {'x-rapidapi-host': 'sportspage-feeds.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'gameId': gameId,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
