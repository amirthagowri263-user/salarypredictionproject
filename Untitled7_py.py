{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNK+Cc7xBcOrccA8CNo/ofG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/amirthagowri263-user/salarypredictionproject/blob/main/Untitled7_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ghQXJaEYgY6S"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv(\"salaryprediction.csv\")\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "88Z7kp3jhVOQ",
        "outputId": "bd6ef7aa-deaf-497b-8a5f-b3447ff4e31a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0  YearsExperience  Salary\n",
              "0           0              1.2   39344\n",
              "1           1              1.4   46206\n",
              "2           2              1.6   37732\n",
              "3           3              2.1   43526\n",
              "4           4              2.3   39892"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2f4d6644-bc00-430e-96cb-331059bcc6c3\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>YearsExperience</th>\n",
              "      <th>Salary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>1.2</td>\n",
              "      <td>39344</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1.4</td>\n",
              "      <td>46206</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>1.6</td>\n",
              "      <td>37732</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>2.1</td>\n",
              "      <td>43526</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>2.3</td>\n",
              "      <td>39892</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2f4d6644-bc00-430e-96cb-331059bcc6c3')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-2f4d6644-bc00-430e-96cb-331059bcc6c3 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-2f4d6644-bc00-430e-96cb-331059bcc6c3');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 30,\n  \"fields\": [\n    {\n      \"column\": \"Unnamed: 0\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 8,\n        \"min\": 0,\n        \"max\": 29,\n        \"num_unique_values\": 30,\n        \"samples\": [\n          27,\n          15,\n          23\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"YearsExperience\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.837888157662719,\n        \"min\": 1.2,\n        \"max\": 10.6,\n        \"num_unique_values\": 28,\n        \"samples\": [\n          4.0,\n          9.7,\n          3.8\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Salary\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 27414,\n        \"min\": 37732,\n        \"max\": 122392,\n        \"num_unique_values\": 30,\n        \"samples\": [\n          112636,\n          67939,\n          113813\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.info())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XVrEHHZRhc9y",
        "outputId": "49d594e5-2261-4b3d-9e8f-0ea95f902a35"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 30 entries, 0 to 29\n",
            "Data columns (total 3 columns):\n",
            " #   Column           Non-Null Count  Dtype  \n",
            "---  ------           --------------  -----  \n",
            " 0   Unnamed: 0       30 non-null     int64  \n",
            " 1   YearsExperience  30 non-null     float64\n",
            " 2   Salary           30 non-null     int64  \n",
            "dtypes: float64(1), int64(2)\n",
            "memory usage: 852.0 bytes\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WGNlxEX0hjJ2",
        "outputId": "c2d2d72b-bfae-4264-be8e-1137fd441395"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       Unnamed: 0  YearsExperience         Salary\n",
            "count   30.000000        30.000000      30.000000\n",
            "mean    14.500000         5.413333   76004.000000\n",
            "std      8.803408         2.837888   27414.429785\n",
            "min      0.000000         1.200000   37732.000000\n",
            "25%      7.250000         3.300000   56721.750000\n",
            "50%     14.500000         4.800000   65238.000000\n",
            "75%     21.750000         7.800000  100545.750000\n",
            "max     29.000000        10.600000  122392.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jcLa3X9Yi_lM",
        "outputId": "3f8d81d3-ab24-4a75-e82a-60751416f739"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Unnamed: 0         0\n",
            "YearsExperience    0\n",
            "Salary             0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(df[\"YearsExperience\"], df[\"Salary\"])\n",
        "plt.xlabel(\"Years Experience\")\n",
        "plt.ylabel(\"Salary\")\n",
        "plt.title(\"Experience vs Salary\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 416
        },
        "id": "36p7PyzDjCjl",
        "outputId": "85e9759e-e921-4db1-ca4e-ff3c1123504b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlUAAAHHCAYAAACWQK1nAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAATfZJREFUeJzt3X18zvX////7sc1OjG1O3juTt5acNJSzsCKVsam82yedEPGWzkSR6o13ZURE6VdKRO936k2FTtRUK6EUM2ctlggtpM1iHHPSnOx4/v7w3ZGjbcy8tuPYjtv1cjkul47X63m8Xo/jpRz3nq/n6/m0GWOMAAAAcEF83F0AAABAdUCoAgAAsAChCgAAwAKEKgAAAAsQqgAAACxAqAIAALAAoQoAAMAChCoAAAALEKoAAAAsQKgCUOWMGzdONpvN3WV4JZvNpnHjxrm7DMAjEaoALzR37lzZbLZSX2vWrHF3ibBISkqKunbtqvDwcNWsWVOXXHKJbr/9dqWmprq7NKDa8XN3AQDc5+mnn1ZMTEyx7Zdeeqkbqim7J598UqNHj3Z3GR7v+eef1+OPP66uXbtqzJgxqlmzpnbs2KEvv/xS7777rhITE91dIlCtEKoAL9azZ0+1b9/e3WWU2dGjRxUcHCw/Pz/5+fHX19mcOnVKEyZMUPfu3fXFF18U25+bm+uGqlwV/XkC1QW3/wCUKjk5WT4+Plq2bJnL9vvuu0/+/v76/vvvJUlfffWVbDabFixYoH//+9+KjIxUcHCw/vGPf2jPnj3Fjpuenq7ExESFhoaqZs2a6tq1q1atWuXSpmjc1JYtW3TnnXeqTp066ty5s8u+v5o3b57atWunoKAg1a1bV3369Cl2/muvvVYtW7bUli1bdN1116lmzZpq0KCBpk6dWux4BQUFGjdunJo2barAwEBFRUXplltu0c6dO51tHA6HXnzxRbVo0UKBgYGKiIjQ/fffr4MHD5712j7//POy2WzatWtXsX1jxoyRv7+/8xjbt29X7969FRkZqcDAQF100UXq06eP7HZ7qcffv3+/8vPzdfXVV5e4Pzw83PnPJ06c0NixY9WuXTuFhoYqODhYXbp00YoVK876HSRp165devDBB9WsWTMFBQWpXr16uu222/TLL7+4tCu65fz111/rwQcfVHh4uC666CKtWLFCNptNH374YbFjv/3227LZbEpLSztnHYAnIFQBXsxut2v//v0urwMHDjj3P/nkk2rdurUGDx6sw4cPS5I+//xzzZkzR2PHjtUVV1zhcrxnnnlGn3zyiUaNGqWHH35YS5cuVXx8vP744w9nm+XLl+uaa65Rfn6+kpOTNWnSJB06dEjXX3+91q5dW6zG2267TceOHdOkSZN07733lvpdnnnmGQ0YMEBNmjTRCy+8oBEjRmjZsmW65pprdOjQIZe2Bw8eVGJioq644gpNmzZNzZs316hRo/TZZ5852xQWFuqmm27S+PHj1a5dO02bNk3Dhw+X3W5XZmams93999+vxx9/XFdffbVeeuklDRo0SPPnz1dCQoJOnjxZar233367bDabFi5cWGzfwoUL1aNHD9WpU0cnTpxQQkKC1qxZo4ceekgzZszQfffdp59//rnY9zpTeHi4goKClJKSory8vFLbSVJ+fr5ef/11XXvttZoyZYrGjRun33//XQkJCcrIyDjrZ9etW6fVq1erT58+mj59uh544AEtW7ZM1157rY4dO1as/YMPPqgtW7Zo7NixGj16tK699lo1bNhQ8+fPL9Z2/vz5aty4seLi4s5aA+AxDACv88YbbxhJJb4CAgJc2m7evNn4+/ube+65xxw8eNA0aNDAtG/f3pw8edLZZsWKFUaSadCggcnPz3duX7hwoZFkXnrpJWOMMQ6HwzRp0sQkJCQYh8PhbHfs2DETExNjunfv7tyWnJxsJJm+ffsWq79oX5FffvnF+Pr6mmeeeaZY7X5+fi7bu3btaiSZt956y7nt+PHjJjIy0vTu3du57b///a+RZF544YVi5y+q/ZtvvjGSzPz58132p6amlrj9r+Li4ky7du1ctq1du9alvu+++85IMosWLTrrsUoyduxYI8kEBwebnj17mmeeecZs2LChWLtTp06Z48ePu2w7ePCgiYiIMHfffbfLdkkmOTnZ+f7YsWPFjpeWllbsGhf9O9e5c2dz6tQpl/ZjxowxAQEB5tChQ85tubm5xs/Pz+VcgKejpwrwYjNmzNDSpUtdXmf21khSy5YtNX78eL3++utKSEjQ/v379eabb5Y4pmnAgAGqXbu28/2tt96qqKgoffrpp5KkjIwMbd++XXfeeacOHDjg7B07evSounXrppUrV8rhcLgc84EHHjjn9/jggw/kcDh0++23u/S6RUZGqkmTJsVuY9WqVUv9+/d3vvf391eHDh30888/O7e9//77ql+/vh566KFi5yu69bho0SKFhoaqe/fuLudt166datWqdc7bZ3fccYc2bNjgcjtxwYIFCggI0M033yxJCg0NlXS6h7Cknp+zGT9+vN5++221adNGn3/+uZ544gm1a9dObdu21Y8//uhs5+vrK39/f0mnb2fm5eXp1KlTat++vTZu3HjWcwQFBTn/+eTJkzpw4IAuvfRShYWFlfjZe++9V76+vi7bBgwYoOPHj+u9995zuQ6nTp1y+XMCPB0jPQEv1qFDhzINVH/88cf17rvvau3atZo0aZJiY2NLbNekSROX9zabTZdeeqlzfM327dslSQMHDiz1XHa7XXXq1HG+L+npxL/avn27jDHFzl+kRo0aLu8vuuiiYmOy6tSpo02bNjnf79y5U82aNTvrgPjt27fLbre7jE8607kGg992220aOXKkcyyaMUaLFi1Sz549FRISIun09x85cqReeOEFzZ8/X126dNE//vEP9e/f3xm4zqZv377q27ev8vPzlZ6errlz5+rtt99Wr169lJmZqcDAQEnSm2++qWnTpmnr1q0uty3Pdf3/+OMPTZ48WW+88Yb27t0rY4xzX0ljvko6XvPmzXXllVdq/vz5Gjx4sKTTt/46derk8U+iAmciVAE4p59//tkZiDZv3lzu4xT1Qj333HNq3bp1iW1q1arl8v7MnpCzHddms+mzzz4r1gtS0jFLaiPJJRCUhcPhUHh4eInjgSTpb3/721k/Hx0drS5dumjhwoX697//rTVr1mj37t2aMmWKS7tp06bpn//8pz766CN98cUXevjhhzV58mStWbNGF110UZlqDQkJUffu3dW9e3fVqFFDb775ptLT09W1a1fNmzdP//znP5WUlKTHH39c4eHh8vX11eTJk1160Ury0EMP6Y033tCIESMUFxen0NBQ2Ww29enTp1ivo1T6n+eAAQM0fPhw/frrrzp+/LjWrFmjV155pUzfDfAUhCoAZ+VwOPTPf/5TISEhGjFihCZNmqRbb71Vt9xyS7G2RcGriDFGO3bs0OWXXy5Jaty4saTTP/Dx8fGW1di4cWMZYxQTE6OmTZtadsz09HSdPHmyWE/XmW2+/PJLXX311WUKfyW544479OCDD2rbtm1asGCBatasqV69ehVr16pVK7Vq1UpPPvmkVq9erauvvlqzZs3SxIkTz/uc7du315tvvqns7GxJ0nvvvadLLrlEH3zwgUsPXnJy8jmP9d5772ngwIGaNm2ac1tBQcFZB9GXpE+fPho5cqTeeecd/fHHH6pRo4buuOOO8zoG4G6MqQJwVi+88IJWr16t2bNna8KECbrqqqs0ZMgQ7d+/v1jbt956y/mUoHT6Bzc7O1s9e/aUJLVr106NGzfW888/ryNHjhT7/O+//16uGm+55Rb5+vpq/PjxxXqbjDEuTzSWVe/evbV///4Se0uKznH77bersLBQEyZMKNbm1KlTZQoWvXv3lq+vr9555x0tWrRIN910k8vcTfn5+Tp16pTLZ1q1aiUfHx8dP3681OMeO3as1KkIisbNNWvWTNKfPXdnXrv09PQyTWXg6+tb7Jq//PLLKiwsPOdnz1S/fn317NlT8+bN0/z585WYmKj69euf1zEAd6OnCvBin332mbZu3Vps+1VXXaVLLrlEP/74o5566in985//dPaezJ07V61bt9aDDz5YbDqAunXrqnPnzho0aJD27dunF198UZdeeqlzKgQfHx+9/vrr6tmzp1q0aKFBgwapQYMG2rt3r1asWKGQkBClpKSc9/do3LixJk6cqDFjxuiXX35RUlKSateuraysLH344Ye677779Nhjj53XMQcMGKC33npLI0eO1Nq1a9WlSxcdPXpUX375pR588EHdfPPN6tq1q+6//35NnjxZGRkZ6tGjh2rUqKHt27dr0aJFeumll3Trrbee9Tzh4eG67rrr9MILL+jw4cPFemeWL1+uYcOG6bbbblPTpk116tQp/e9//5Ovr6969+5d6nGPHTumq666Sp06dVJiYqIaNmyoQ4cOafHixfrmm2+UlJSkNm3aSJJuuukmffDBB/q///s/3XjjjcrKytKsWbMUGxtbYvg900033aT//e9/Cg0NVWxsrNLS0vTll1+qXr16ZbzSfxowYIDzepUUVAGP56anDgG40dmmVJBk3njjDXPq1Clz5ZVXmosuusjlUXdjjHnppZeMJLNgwQJjzJ9TKrzzzjtmzJgxJjw83AQFBZkbb7zR7Nq1q9j5v/vuO3PLLbeYevXqmYCAANOoUSNz++23m2XLljnbFE2b8Pvvvxf7/F+nVCjy/vvvm86dO5vg4GATHBxsmjdvboYOHWq2bdvmbNO1a1fT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K/Z64IEH3F2aJOmDDz7QhAkT3F0GgLNgRnUAFW7Pnj1q1aqVpkyZovvvv1/S6TXCWrVqpZkzZ+quu+6y9HwnT55UjRo1zusz1157rZo2baqnn37aZXvNmjUVEhJiZXnn5cSJE/L393fb+QGUHT1VACpcw4YN9dJLL+mxxx5TVlaWjDEaPHiwevTooTZt2qhnz56qVauWIiIidNddd2n//v3Oz6ampqpz584KCwtTvXr1dNNNN2nnzp3O/b/88otsNpsWLFigrl27KjAwUPPnz9euXbvUq1cv1alTR8HBwWrRooU+/fTTs9ZZs2ZNRUZGuryKAtVbb72lWrVqafv27c72Dz74oJo3b65jx45Jki6++GJNmDBBffv2VXBwsBo0aKAZM2a4nOPQoUO655579Le//U0hISG6/vrr9f333zv3jxs3Tq1bt9brr7+umJgYBQYGSip+++/48eN67LHH1KBBAwUHB6tjx4766quvnPvnzp2rsLAwff7557rssstUq1YtJSYmKjs726We//73v2rRooUCAgIUFRWlYcOGlblWAK4IVQAqxcCBA9WtWzfdfffdeuWVV5SZmanXXntN119/vdq0aaP169crNTVV+/bt0+233+783NGjRzVy5EitX79ey5Ytk4+Pj/7v//5PDofD5fijR4/W8OHD9eOPPyohIUFDhw7V8ePHtXLlSm3evFlTpkxRrVq1yl3/gAEDdMMNN6hfv346deqUPvnkE73++uuaP3++atas6Wz33HPP6YorrtB3333nrGnp0qXO/bfddptyc3P12WefacOGDWrbtq26deumvLw8Z5sdO3bo/fff1wcffKCMjIwS6xk2bJjS0tL07rvvatOmTbrtttuUmJjoEvqOHTum559/Xv/73/+0cuVK7d69W4899phz/8yZMzV06FDdd9992rx5sz7++GNdeuml51UrgDO4czVnAN5l3759pn79+sbHx8d8+OGHZsKECaZHjx4ubfbs2WMklbqS/e+//24kmc2bNxtjjMnKyjKSzIsvvujSrlWrVmbcuHFlrq1r166mRo0aJjg42OU1b948Z5u8vDxz0UUXmSFDhpiIiAjzzDPPuByjUaNGJjEx0WXbHXfcYXr27GmMMeabb74xISEhpqCgwKVN48aNzWuvvWaMMSY5OdnUqFHD5ObmFqtv+PDhxhhjdu3aZXx9fc3evXtd2nTr1s2MGTPGGGPMG2+8YSSZHTt2OPfPmDHDREREON9HR0ebJ554osTrUZZaAbjyc2+kA+BNwsPDdf/992vx4sVKSkrS/PnztWLFihJ7kHbu3KmmTZtq+/btGjt2rNLT07V//35nD9Xu3bvVsmVLZ/v27du7fP7hhx/WkCFD9MUXXyg+Pl69e/fW5Zdfftb6+vXrpyeeeMJlW0REhPOf69Spo//85z9KSEjQVVddpdGjRxc7RlxcXLH3L774oiTp+++/15EjR1SvXj2XNn/88YfLLc1GjRrpb3/7W6l1bt68WYWFhWratKnL9uPHj7scu2bNmmrcuLHzfVRUlHJzcyVJubm5+u2339StW7cSz1HWWgH8iVAFoFL5+fnJz+/0Xz1HjhxRr169NGXKlGLtoqKiJEm9evVSo0aNNGfOHEVHR8vhcKhly5Y6ceKES/vg4GCX9/fcc48SEhL0ySef6IsvvtDkyZM1bdo0PfTQQ6XWFhoa6nL7qyQrV66Ur6+vsrOzdfToUdWuXbtM31s6/X2joqJcxj4VCQsLK/W7lHQcX19fbdiwQb6+vi77zgyofx2sb7PZZP7fs0lBQUGW1ArgT4QqAG7Ttm1bvf/++7r44oudQetMBw4c0LZt2zRnzhx16dJFkvTtt9+W+fgNGzbUAw88oAceeEBjxozRnDlzzhqqzmX16tWaMmWKUlJSNGrUKA0bNkxvvvmmS5s1a9YUe3/ZZZdJOv19c3Jy5Ofnp4svvrjcdbRp00aFhYXKzc11XpfzVbt2bV188cVatmyZrrvuumL7raoV8CYMVAfgNkOHDlVeXp769u2rdevWaefOnfr88881aNAgFRYWqk6dOqpXr55mz56tHTt2aPny5Ro5cmSZjj1ixAh9/vnnysrK0saNG7VixQpnuCnNsWPHlJOT4/I6ePCgJOnw4cO666679PDDD6tnz56aP3++FixYoPfee8/lGKtWrdLUqVP1008/acaMGVq0aJGGDx8uSYqPj1dcXJySkpL0xRdf6JdfftHq1av1xBNPaP369WW+bk2bNlW/fv00YMAAffDBB8rKytLatWs1efJkffLJJ2U+zrhx4zRt2jRNnz5d27dv18aNG/Xyyy9bWivgTQhVANwmOjpaq1atUmFhoXr06KFWrVppxIgRCgsLk4+Pj3x8fPTuu+9qw4YNatmypR555BE999xzZTp2YWGhhg4dqssuu0yJiYlq2rSpXn311bN+Zs6cOYqKinJ59e3bV5I0fPhwBQcHa9KkSZKkVq1aadKkSbr//vu1d+9e5zEeffRRrV+/Xm3atNHEiRP1wgsvOCc+tdls+vTTT3XNNddo0KBBatq0qfr06aNdu3a5jN0qizfeeEMDBgzQo48+qmbNmikpKUnr1q3T3//+9zIfY+DAgXrxxRf16quvqkWLFrrpppucTw9aWSvgLZj8EwAscvHFF2vEiBEsJwN4KXqqAAAALECoAgAAsAC3/wAAACxATxUAAIAFCFUAAAAWIFQBAABYgFAFAABgAUIVAACABQhVAAAAFiBUAQAAWIBQBQAAYAFCFQAAgAX+fwiA7hJWE1chAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = df[[\"YearsExperience\"]]\n",
        "y = df[\"Salary\"]"
      ],
      "metadata": {
        "id": "LDaCvPn_jHhF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size=0.2,\n",
        "    random_state=42\n",
        ")"
      ],
      "metadata": {
        "id": "h8WO6FCbjr89"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "model = LinearRegression()\n",
        "\n",
        "model.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        },
        "id": "3llrS3q6jw5K",
        "outputId": "b493c8f7-a476-4c3c-9be6-48a16db3d859"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {\n",
              "  /* Definition of color scheme common for light and dark mode */\n",
              "  --sklearn-color-text: #000;\n",
              "  --sklearn-color-text-muted: #666;\n",
              "  --sklearn-color-line: gray;\n",
              "  /* Definition of color scheme for unfitted estimators */\n",
              "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
              "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
              "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
              "  --sklearn-color-unfitted-level-3: chocolate;\n",
              "  /* Definition of color scheme for fitted estimators */\n",
              "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
              "  --sklearn-color-fitted-level-1: #d4ebff;\n",
              "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
              "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
              "\n",
              "  /* Specific color for light theme */\n",
              "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
              "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
              "  --sklearn-color-icon: #696969;\n",
              "\n",
              "  @media (prefers-color-scheme: dark) {\n",
              "    /* Redefinition of color scheme for dark theme */\n",
              "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
              "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
              "    --sklearn-color-icon: #878787;\n",
              "  }\n",
              "}\n",
              "\n",
              "#sk-container-id-1 {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 pre {\n",
              "  padding: 0;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-hidden--visually {\n",
              "  border: 0;\n",
              "  clip: rect(1px 1px 1px 1px);\n",
              "  clip: rect(1px, 1px, 1px, 1px);\n",
              "  height: 1px;\n",
              "  margin: -1px;\n",
              "  overflow: hidden;\n",
              "  padding: 0;\n",
              "  position: absolute;\n",
              "  width: 1px;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-dashed-wrapped {\n",
              "  border: 1px dashed var(--sklearn-color-line);\n",
              "  margin: 0 0.4em 0.5em 0.4em;\n",
              "  box-sizing: border-box;\n",
              "  padding-bottom: 0.4em;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-container {\n",
              "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
              "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
              "     so we also need the `!important` here to be able to override the\n",
              "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
              "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
              "  display: inline-block !important;\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-text-repr-fallback {\n",
              "  display: none;\n",
              "}\n",
              "\n",
              "div.sk-parallel-item,\n",
              "div.sk-serial,\n",
              "div.sk-item {\n",
              "  /* draw centered vertical line to link estimators */\n",
              "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
              "  background-size: 2px 100%;\n",
              "  background-repeat: no-repeat;\n",
              "  background-position: center center;\n",
              "}\n",
              "\n",
              "/* Parallel-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item::after {\n",
              "  content: \"\";\n",
              "  width: 100%;\n",
              "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
              "  flex-grow: 1;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel {\n",
              "  display: flex;\n",
              "  align-items: stretch;\n",
              "  justify-content: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  position: relative;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
              "  align-self: flex-end;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
              "  align-self: flex-start;\n",
              "  width: 50%;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
              "  width: 0;\n",
              "}\n",
              "\n",
              "/* Serial-specific style estimator block */\n",
              "\n",
              "#sk-container-id-1 div.sk-serial {\n",
              "  display: flex;\n",
              "  flex-direction: column;\n",
              "  align-items: center;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  padding-right: 1em;\n",
              "  padding-left: 1em;\n",
              "}\n",
              "\n",
              "\n",
              "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
              "clickable and can be expanded/collapsed.\n",
              "- Pipeline and ColumnTransformer use this feature and define the default style\n",
              "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
              "*/\n",
              "\n",
              "/* Pipeline and ColumnTransformer style (default) */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable {\n",
              "  /* Default theme specific background. It is overwritten whether we have a\n",
              "  specific estimator or a Pipeline/ColumnTransformer */\n",
              "  background-color: var(--sklearn-color-background);\n",
              "}\n",
              "\n",
              "/* Toggleable label */\n",
              "#sk-container-id-1 label.sk-toggleable__label {\n",
              "  cursor: pointer;\n",
              "  display: flex;\n",
              "  width: 100%;\n",
              "  margin-bottom: 0;\n",
              "  padding: 0.5em;\n",
              "  box-sizing: border-box;\n",
              "  text-align: center;\n",
              "  align-items: start;\n",
              "  justify-content: space-between;\n",
              "  gap: 0.5em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label .caption {\n",
              "  font-size: 0.6rem;\n",
              "  font-weight: lighter;\n",
              "  color: var(--sklearn-color-text-muted);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
              "  /* Arrow on the left of the label */\n",
              "  content: \"▸\";\n",
              "  float: left;\n",
              "  margin-right: 0.25em;\n",
              "  color: var(--sklearn-color-icon);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
              "  color: var(--sklearn-color-text);\n",
              "}\n",
              "\n",
              "/* Toggleable content - dropdown */\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content {\n",
              "  max-height: 0;\n",
              "  max-width: 0;\n",
              "  overflow: hidden;\n",
              "  text-align: left;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content pre {\n",
              "  margin: 0.2em;\n",
              "  border-radius: 0.25em;\n",
              "  color: var(--sklearn-color-text);\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
              "  /* Expand drop-down */\n",
              "  max-height: 200px;\n",
              "  max-width: 100%;\n",
              "  overflow: auto;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
              "  content: \"▾\";\n",
              "}\n",
              "\n",
              "/* Pipeline/ColumnTransformer-specific style */\n",
              "\n",
              "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator-specific style */\n",
              "\n",
              "/* Colorize estimator box */\n",
              "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  /* The background is the default theme color */\n",
              "  color: var(--sklearn-color-text-on-default-background);\n",
              "}\n",
              "\n",
              "/* On hover, darken the color of the background */\n",
              "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "/* Label box, darken color on hover, fitted */\n",
              "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
              "  color: var(--sklearn-color-text);\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Estimator label */\n",
              "\n",
              "#sk-container-id-1 div.sk-label label {\n",
              "  font-family: monospace;\n",
              "  font-weight: bold;\n",
              "  display: inline-block;\n",
              "  line-height: 1.2em;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-label-container {\n",
              "  text-align: center;\n",
              "}\n",
              "\n",
              "/* Estimator-specific */\n",
              "#sk-container-id-1 div.sk-estimator {\n",
              "  font-family: monospace;\n",
              "  border: 1px dotted var(--sklearn-color-border-box);\n",
              "  border-radius: 0.25em;\n",
              "  box-sizing: border-box;\n",
              "  margin-bottom: 0.5em;\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-0);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-0);\n",
              "}\n",
              "\n",
              "/* on hover */\n",
              "#sk-container-id-1 div.sk-estimator:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-2);\n",
              "}\n",
              "\n",
              "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-2);\n",
              "}\n",
              "\n",
              "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
              "\n",
              "/* Common style for \"i\" and \"?\" */\n",
              "\n",
              ".sk-estimator-doc-link,\n",
              "a:link.sk-estimator-doc-link,\n",
              "a:visited.sk-estimator-doc-link {\n",
              "  float: right;\n",
              "  font-size: smaller;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1em;\n",
              "  height: 1em;\n",
              "  width: 1em;\n",
              "  text-decoration: none !important;\n",
              "  margin-left: 0.5em;\n",
              "  text-align: center;\n",
              "  /* unfitted */\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted,\n",
              "a:link.sk-estimator-doc-link.fitted,\n",
              "a:visited.sk-estimator-doc-link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
              ".sk-estimator-doc-link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover,\n",
              "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
              ".sk-estimator-doc-link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "/* Span, style for the box shown on hovering the info icon */\n",
              ".sk-estimator-doc-link span {\n",
              "  display: none;\n",
              "  z-index: 9999;\n",
              "  position: relative;\n",
              "  font-weight: normal;\n",
              "  right: .2ex;\n",
              "  padding: .5ex;\n",
              "  margin: .5ex;\n",
              "  width: min-content;\n",
              "  min-width: 20ex;\n",
              "  max-width: 50ex;\n",
              "  color: var(--sklearn-color-text);\n",
              "  box-shadow: 2pt 2pt 4pt #999;\n",
              "  /* unfitted */\n",
              "  background: var(--sklearn-color-unfitted-level-0);\n",
              "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link.fitted span {\n",
              "  /* fitted */\n",
              "  background: var(--sklearn-color-fitted-level-0);\n",
              "  border: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "\n",
              ".sk-estimator-doc-link:hover span {\n",
              "  display: block;\n",
              "}\n",
              "\n",
              "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link {\n",
              "  float: right;\n",
              "  font-size: 1rem;\n",
              "  line-height: 1em;\n",
              "  font-family: monospace;\n",
              "  background-color: var(--sklearn-color-background);\n",
              "  border-radius: 1rem;\n",
              "  height: 1rem;\n",
              "  width: 1rem;\n",
              "  text-decoration: none;\n",
              "  /* unfitted */\n",
              "  color: var(--sklearn-color-unfitted-level-1);\n",
              "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
              "  /* fitted */\n",
              "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
              "  color: var(--sklearn-color-fitted-level-1);\n",
              "}\n",
              "\n",
              "/* On hover */\n",
              "#sk-container-id-1 a.estimator_doc_link:hover {\n",
              "  /* unfitted */\n",
              "  background-color: var(--sklearn-color-unfitted-level-3);\n",
              "  color: var(--sklearn-color-background);\n",
              "  text-decoration: none;\n",
              "}\n",
              "\n",
              "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
              "  /* fitted */\n",
              "  background-color: var(--sklearn-color-fitted-level-3);\n",
              "}\n",
              "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow\"><div><div>LinearRegression</div></div><div><a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LinearRegression.html\">?<span>Documentation for LinearRegression</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></div></label><div class=\"sk-toggleable__content fitted\"><pre>LinearRegression()</pre></div> </div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test)\n",
        "\n",
        "print(y_pred)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OxHhSY96j0sM",
        "outputId": "e41fdc3b-3382-4ebc-e5fe-7240b3b3600c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[115791.21011287  71499.27809463 102597.86866063  75268.80422384\n",
            "  55478.79204548  60190.69970699]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import mean_absolute_error\n",
        "from sklearn.metrics import mean_squared_error\n",
        "from sklearn.metrics import r2_score"
      ],
      "metadata": {
        "id": "BnlGcd7tj61x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "mae = mean_absolute_error(y_test, y_pred)\n",
        "print(\"MAE:\", mae)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HxdA_4LLj9kN",
        "outputId": "23209a46-699c-4fd4-e439-4866d6284689"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "MAE: 6286.453830757742\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mse = mean_squared_error(y_test, y_pred)\n",
        "print(\"MSE:\", mse)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GUQnLCZfkD5_",
        "outputId": "a8c564eb-a5e8-4619-9905-a6850200e080"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "MSE: 49830096.855908334\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r2 = r2_score(y_test, y_pred)\n",
        "print(\"R2 Score:\", r2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hCYOi7dLkHd7",
        "outputId": "0522e557-4858-40b8-ea6a-6e1d4471ff11"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "R2 Score: 0.9024461774180498\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(X, y)\n",
        "\n",
        "plt.plot(\n",
        "    X,\n",
        "    model.predict(X),\n",
        "    linewidth=2\n",
        ")\n",
        "\n",
        "plt.xlabel(\"Years Experience\")\n",
        "plt.ylabel(\"Salary\")\n",
        "plt.title(\"Salary Prediction\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 416
        },
        "id": "next1xlNk6Fm",
        "outputId": "58874611-2a5f-40ac-d141-452167f6414b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlUAAAHHCAYAAACWQK1nAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAa99JREFUeJzt3XlYVNX/B/D3DMsMsgyCsikirsiigCumWYniRlFmiqZmthm4a+q33NIyNcsd0krr526ZiRpmapmKqCwqLrihorKoyLDJNnN/fxBXR0ABB2aA9+t5eJ4498zcD1PJ23POPUciCIIAIiIiInouUl0XQERERFQbMFQRERERaQFDFREREZEWMFQRERERaQFDFREREZEWMFQRERERaQFDFREREZEWMFQRERERaQFDFREREZEWMFQRkd546aWX8NJLL+m6DL0yZ84cSCQSjbamTZvinXfe0do93nnnHTRt2lRr70dUVzFUEVGlnT17Fm+++SacnJwgl8vRqFEj9OrVCytWrNB1aVojkUjEL6lUCgcHB/Tu3Rt///23rkurkDt37mDOnDmIjY3VdSlEtZahrgsgoprp2LFjePnll9GkSRO8//77sLOzQ2JiIo4fP45ly5Zh7Nixui5Ra3r16oURI0ZAEAQkJCRg9erVeOWVV7Bnzx707du32uuJj4+HVFqxvxPfuXMHc+fORdOmTeHp6alxbe3atVCr1VqskKhuYqgiokr54osvoFAocPLkSVhaWmpcS01N1U1RjyksLIRarYaxsfFzv1erVq3w9ttvi9+//vrraNu2LZYuXVpmqMrNzYWxsXGFw095yGQyrb6fkZGRVt+PqK7i9B8RVcrVq1fh5uZWIlABgI2Njcb369atwyuvvAIbGxvIZDK4uroiJCTkmffIz8/HrFmz0L59eygUCpiamqJ79+44dOiQRr/r169DIpHg66+/xtKlS9G8eXPIZDKcOHECpqamGD9+fIn3vnXrFgwMDLBgwYKK/eAAPDw80KBBAyQkJAAA/v77b0gkEmzZsgWfffYZGjVqhHr16iEjIwMAEBkZiT59+kChUKBevXro0aMHjh49WuJ9jxw5go4dO0Iul6N58+b47rvvSr1/aWuq0tPTMXHiRDRt2hQymQyNGzfGiBEjcO/ePfz999/o2LEjAGDUqFHidOb69esBlL6mKjs7G5MnT4aj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ER4eju7du+Pjjz9GYWEhVqxYATc3N5w5c+ap95k6dSp++eUXDBo0CO+++y7at2+PtLQ07Nq1C6GhoWjXrh2aN28OS0tLhIaGwtzcHKampujcuXOp69D8/f3x8ssv49NPP8X169fRrl07/Pnnn/j9998xYcIEjUXpRPQYXT56SEQ11x9//CG8++67gouLi2BmZiYYGxsLLVq0EMaOHSukpKRo9N21a5fQtm1bQS6XC02bNhUWLlwo/PjjjwIAISEhQez35JYKarVa+PLLLwUnJydBJpMJXl5ewu7du0tsAVC8pcLixYufWnO/fv0EAMKxY8fK/XMCEIKCgp7ap3hLhe3bt5d6PSYmRnjjjTcEa2trQSaTCU5OTsJbb70lHDhwQKPfP//8I7Rv314wNjYWmjVrJoSGhgqzZ89+5pYKgiAI9+/fF4KDg4VGjRoJxsbGQuPGjYWRI0cK9+7dE/v8/vvvgqurq2BoaKixvcKTn6cgCEJmZqYwceJEwcHBQTAyMhJatmwpLF68WGNriKd9PqXVSFTbSQSBKwmJqG54/fXXcfbsWVy5ckXXpRBRLcQ1VURUJyQlJWHPnj0YPny4rksholqKa6qIqFZLSEjA0aNH8f3338PIyAgffvihrksiolqKI1VEVKv9888/GD58OBISEvDTTz/Bzs5O1yURUS3FNVVEREREWsCRKiIiIiItYKgiIiIi0gIuVK9GarUad+7cgbm5eaVOjiciIqLqJwgCMjMz4eDgAKm07PEohqpqdOfOHTg6Ouq6DCIiIqqExMRENG7cuMzrDFXVqPhg0sTERFhYWOi4GiIiIiqPjIwMODo6ahwwXhqGqmpUPOVnYWHBUEVERFTDPGvpDheqExEREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWkBQxURERHVCoIg6PT+DFVERERU4525lY7XVx9DkvKhzmpgqCIiIqIaSxAErDuagIEhxxCbmI5xm2NQqFLrpBZDndyViIiI6Dkpcwrwya+nse9citiWrxKgfFgAazNZtdfDUEVEREQ1TszNBwjeFIPb6Y+m+97v7oypfi4wNtTNRBxDFREREektlVrAiYQ0pGbmwsZcjo5N62Pd0etYGH4RheqihemW9YywZFA79Gxjq9NaGaqIiIhIL4XHJWFu2HkkKXPFNpmhFHmFj9ZMdXCqj+WBXnCwNNFFiRoYqoiIiEjvhMclYcyGaDy5ScLjgerjl5pjYq9WkEokiLh6XxzN6uRsBQOppHoLBkMVERER6RmVWsDcsPMlAtXjrOoZYXLv1th/PrnEaJa9Qo7Z/q7o425f9cU+hlsqEBERkV45kZCmEZJKk5ZTgJUHr2DMhugSfZOVuRizIRrhcUlVWWYJDFVERESkV1Iznx6oiq07mlDqaFZx29yw81Cpq2+XdYYqIiIi0hsqtYAjl++Vq2/6w4IyrwkAkpS5OJGQpqXKno1rqoiIiEgvpGbmYuLWWBy9cv+p/SQAFCZGTw1Vj79ndeFIFREREenc0Sv30G/ZETFQScp4eK+4edQLTcv1vjbm8ucvrpwYqoiIiEhnVGoB3/wZj7d/iMS9rDwAgK2FDJvf74LQt71hr9AMRXYKOULe9kbwKy1hr5CjrI0TJCh6CrCTs1XV/gCP0WmoOnz4MPz9/eHg4ACJRIKdO3eK1woKCjBt2jR4eHjA1NQUDg4OGDFiBO7cuaPxHmlpaRg2bBgsLCxgaWmJ0aNHIysrS6PPmTNn0L17d8jlcjg6OmLRokUlatm+fTtcXFwgl8vh4eGBvXv3alwXBAGzZs2Cvb09TExM4Ovri8uXL2vvwyAiIqpjUjJyMXTtcSw/eAXCf+vJX2zVEHvHdUeXZtbo426PI9Neweb3u2DZEE9sfr8Ljkx7BX3c7WEglWC2vysAlAhWxd/P9net1v2qdBqqsrOz0a5dO6xatarEtZycHERHR2PmzJmIjo7Gjh07EB8fj1dffVWj37Bhw3Du3Dns378fu3fvxuHDh/HBBx+I1zMyMtC7d284OTkhKioKixcvxpw5c7BmzRqxz7FjxxAYGIjRo0cjJiYGAQEBCAgIQFxcnNhn0aJFWL58OUJDQxEZGQlTU1P4+fkhN7f65mqJiIhqi38u3UXfZf8i8r+F5AZSCT7p0xrr3+mocRiygVQCn+bWeM2zEXyaW2uEpD7u9gh52xt2ZYxmVfc+VRJBEKrvWcOnkEgk+O233xAQEFBmn5MnT6JTp064ceMGmjRpggsXLsDV1RUnT55Ehw4dAADh4eHo168fbt26BQcHB4SEhODTTz9FcnIyjI2NAQDTp0/Hzp07cfHiRQDA4MGDkZ2djd27d4v36tKlCzw9PREaGgpBEODg4IDJkydjypQpAAClUglbW1usX78eQ4YMKdfPmJGRAYVCAaVSCQsLi8p8TERERDVaoUqNJfsvIeTvq2KbvUKOFYFe6NC0clN1T54PqO0d1cv7+7tGralSKpWQSCSwtLQEAERERMDS0lIMVADg6+sLqVSKyMhIsc+LL74oBioA8PPzQ3x8PB48eCD28fX11biXn58fIiIiAAAJCQlITk7W6KNQKNC5c2exT2ny8vKQkZGh8UVERFRX3Ul/iCFrjmsEqp4uNtg7rnulAxXw9NGs6lRjQlVubi6mTZuGwMBAMSUmJyfDxsZGo5+hoSGsrKyQnJws9rG11Ty1uvj7Z/V5/PrjryutT2kWLFgAhUIhfjk6OlboZyYiIqotDl5MQb/l/+LUjaIBDUOpBJ/2a4PvR3ZAfVPjZ7y6ZqgRoaqgoABvvfUWBEFASEiIrssptxkzZkCpVIpfiYmJui6JiIioWhWo1Phiz3m8u/4U0nOK9pVqZGmCbR/54P0Xm0FS1t4JNZDeb/5ZHKhu3LiBgwcPasxl2tnZITU1VaN/YWEh0tLSYGdnJ/ZJSUnR6FP8/bP6PH69uM3e3l6jj6enZ5m1y2QyyGSyMq8TERHVZolpORi7OQaxieliW29XWyx+sx0U9Yx0V1gV0euRquJAdfnyZfz111+wtrbWuO7j44P09HRERUWJbQcPHoRarUbnzp3FPocPH0ZBwaNdV/fv34/WrVujfv36Yp8DBw5ovPf+/fvh4+MDAHB2doadnZ1Gn4yMDERGRop9iIiI6JF955LRf/m/YqAyMijaAuG74e1rZaACdDxSlZWVhStXrojfJyQkIDY2FlZWVrC3t8ebb76J6Oho7N69GyqVSly/ZGVlBWNjY7Rp0wZ9+vTB+++/j9DQUBQUFCA4OBhDhgyBg4MDAGDo0KGYO3cuRo8ejWnTpiEuLg7Lli3Dt99+K953/Pjx6NGjB5YsWYL+/ftjy5YtOHXqlLjtgkQiwYQJEzB//ny0bNkSzs7OmDlzJhwcHJ76tCIREVFdk1eowoK9F7H+2HWxrYlVPawc6oW2jS11Vle1EHTo0KFDAorOPNT4GjlypJCQkFDqNQDCoUOHxPe4f/++EBgYKJiZmQkWFhbCqFGjhMzMTI37nD59WujWrZsgk8mERo0aCV999VWJWrZt2ya0atVKMDY2Ftzc3IQ9e/ZoXFer1cLMmTMFW1tbQSaTCT179hTi4+Mr9PMqlUoBgKBUKiv0OiIioprg+r0sYcDyfwWnabvFrzEbTgnKh/m6Lu25lPf3t97sU1UXcJ8qIiKqrfacScL0X88gM68QAGBsKMXMAa54u3OTGr8Yvby/v/V+oToRERFVrefZPDO3QIX5e85jw/GbYptzA1OsHOoFNwdFVZWslxiqiIiI6rDwuCTMDTuPJOWjY9fsFXLM9nd95jEvCfeyEbQxGueTHm1u/Wo7B3z5hgfMZHUvYuj1039ERERUdcLjkjBmQ7RGoAKAZGUuxmyIRnhcUpmv/T32NgYs/1cMVDJDKb56wwPLhnjWyUAFcKSKiIioTlKpBcwNO4/SFlYLACQA5oadRy9XO42pwNwCFebsOoctJx9taN28oSlWDfOGi13dXi/MUEVERFQHnUhIKzFC9TgBQJIyFycS0uDTvGifyCupmQjaGIP4lEyx3xvejTDvNXeY1tHRqcfxEyAiIqqDUjPLDlSl9fs16hY+2xmHhwUqAICJkQE+f80NgzrwXNtiDFVERER1kI25vFz9LORGmLL9NH6JuiW2tbI1w6qh3mhpa15V5dVIDFVERER1UCdnK9gr5EhW5pa6rkoCwNrMGF/suYArd7PE9sEdHDHnVTeYGBtUW601BZ/+IyIiqoMMpEVn8QFFAepJAgDlwwIxUNUzNsDSwZ5Y+GZbBqoyMFQRERHVUX3c7RHytjfsFJpTgXKjonhQoCoaw2pjb4HdY7shwKtRtddYk3D6j4iIqA7r426PXq52OJGQhpibD/B/x29oPBU4rHMTzBzgCrkRR6eehaGKiIiojpNKgKt3s7D0wGXkF6oBAGYyQ3w10AMD2jrouLqag6GKiIjoP89zBl5NlZlbgOk7zmLPmUe7p7s3ssCqod5wsjbVYWU1D0MVERERnu8MvJrq7C0lgjdH48b9HLHtna5NMaOfC2SGnO6rKC5UJyKiOu95zsCriQRBwPqjCRgYckwMVOZyQ4S+7Y05r7oxUFUSR6qIiKhOq+wZeDWVMqcAn/x6GvvOpYht7RwtsTLQC45W9XRYWc3HUEVERHVaZc7Aq6liE9MRvCkatx48FNve6+aMT/q4wNhQc/KqLq4ve14MVUREVKdV9Ay8mkgQBPxwJAFf/XERheqiMTmFiRGWDGoHX1fbEv3r4voybeCaKiIiqtPKewZeefvpm/ScfLz/8ynM33NBDFTtnepj7/juZQaqurS+TJsYqoiIqE4rPgOvrIktCYpGaTo5W1VnWVoRdSMN/Zb9i78upIptH/Voji0fdEEjS5MS/Z+1vgwoWl+mUpfWgxiqiIioTnvaGXjF38/2d61R64nUagEhf1/FW98dx53/RpysTI2xblRHTO/rAiOD0n/9V2R9GZXEUEVERHVeWWfg2SnkCHnbu0atI7qflYdR609iYfhFcUSpU1Mr7B3XHS+3tnnqa+vC+rKqxIXqRERE0DwDr6Y+8RZ57T7GbYlBSkYeAEAiAYJfboHxPVvCsIzRqcfV9vVlVY2hioiI6D8GUkmN3DZBpRaw+tAVfPvXJRQvd2pgZoylg73QrWWDcr9P8fqyZGVuqeuqJCgavauJ68uqA6f/iIiIarC7mXkY+eMJLNn/KFB1bW6NveO6VyhQAbVzfVl1YqgiIiKqoY5duYe+y/7FkSv3AABSCTDRtxX+b3Rn2FhUboquNq0vq26c/iMiIqphVGoByw5cxoqDlyH8NzplYy7DsiFeWpm+rA3ry3SBoYqIiKgGScnIxfgtMTh+7dG2Bt1bNsC3gz3RwEymtfvU1PVlusRQRUREVE2e9zy9fy7dxaStsbifnQ+gKPhM6tUKY3o0h5SjSDrHUEVERFQNnuc8vUKVGt/sv4TVf18V2+ws5Fgx1Asdm/JJPH3BhepERERV7HnO07uT/hBD1hzXCFQvt26IveO7M1DpGY5UERERVaFnnacnQdF5er1c7UpMBR68mIJJ204jPacAAGAoleCTPq3xXrdmnO7TQwxVREREVagi5+kVLwwvUKmxeF881hy+JvZrZGmCFUO94N2kflWXTJXEUEVERFSFKnqeXmJaDsZujkFsYrp4rZerLRa/2RaW9YyrokTSEoYqIiKiKlSR8/T2nUvG1O2nkZFbCAAwMpBget82ePeFppBION2n7xiqiIiIqlB5ztOztZBh37lkrD92XWx3tDLBykBvtHO0rKZK6Xnx6T8iIqIq9Kzz9AQAMkMDjUDV190Ou8d2Z6CqYRiqiIiIqlhZ5+kp6hlBbiTFjbQcAICxgRTzXnPD6mHeUJgY6aJUeg6c/iMiIqoGj5+ndzs9B+FxKfjrQop4val1Pawc6g33RgodVknPg6GKiIiomhhIJbBTyDFv93mcT8oQ219t54Av3/CAmYy/lmsy/tsjIiKqJr/H3sb/dpxFdr4KACAzlGLOq24Y0tGRT/fVAgxVREREVSy3QIU5u85hy8lEsa1ZQ1OsGuqNNvYWOqyMtImhioiIqApdSc1E0MYYxKdkim1veDXCvAB3mHK6r1bhv00iIqIq8mvULXy2Mw4PC4qm++RGUsx7zR2DOjhW6H1UagEnEtKQmpkLG3M5OjlblTgnkHSPoYqIiEjLcvILMev3c/gl6pbY1srWDKuGeqOlrXmF3is8Lglzw85rnB9or5Bjtr8r+rjba61men7cp4qIiEiL4pMz8erKoxqB6q0OjfF7ULdKBaoxG6JLHMicrMzFmA3RCI9L0krNpB0cqSIiItICQRCw7VQiZu86h9wCNQCgnrEBvnjdHa97Na7w+6nUAuaGnS/1aBsBRbuxzw07j16udpwK1BMMVURERM8pK68Qn/12Fjtj74htLnbmWDXMG80bmlXqPU8kpJUYoXqcACBJmYsTCWnwaW5dqXuQdjFUERERPYfzdzIQvCka1+5li21DOzfBrAGukBsZVPp9UzPLDlSV6UdVj6GKiIioEgRBwMbIm/h893nkFxZN95nJDLHgDQ/4t3N47ve3MZc/u1MF+lHVY6giIiKqoIzcAszYcRZ7zjxaKO7eyAIrA73RtIGpVu7RydkK9go5kpW5pa6rkgCwUxRtr0D6gU//ERERVcDZW0r4rziiEaje6doUv47pqrVABRSdEzjb3xVAUYB6XPH3s/1duUhdjzBUERERlYMgCFh/NAEDQ47hxv0cAIC53BChb3tjzqtukBlWfv1UWfq42yPkbW/YKTSn+OwUcoS87c19qvQMp/+IiIieQZlTgE9+PY1951LEtnaNFVg51BuOVvWq9N593O3Ry9WOO6rXAAxVRERETxGbmI7gTdG49eCh2Da6mzOm9XGBsWH1TPgYSCXcNqEGYKgiIiIqhSAI+OFIAr764yIK1UVLxRUmRvh6UDv0crXVcXWkjxiqiIiInpCek48p20/jrwupYpt3E0usGOqNRpYmOqyM9BlDFRER0WOibqRh7KYY3HlsN/MPezTDlN6tYWTA57uobAxVREREANRqAd8dvoav/4yH6r/pvvr1jPDNW5542cVGx9VRTcBQRUREtY5KLVToabn7WXmYvP00/o6/K7Z1amqFZYGesFdwuo/Kh6GKiIhqlfC4JMwNO69xGLG9Qo7Z/q6l7usUee0+xm2JQUpGHgBAIgE+fqk5Jvq2giGn+6gC+F8LERHVGuFxSRizIVojUAFAsjIXYzZEIzzu0S7oKrWAFQcuI3DtcTFQNTAzxs/vdsJUPxcGKqowjlQREVGtoFILmBt2vtRz8gQUHe0yN+w8ernaIS07HxO3xuLIlXtiH59m1lg2xBM2FjygmCqHoYqIiGqFEwlpJUaoHicASFLm4scjCVjz7zXczXw03Te+Z0uMfaUldymn58JQRUREtUJqZtmB6nFf7r0gjmY1NJdh2RBPdG3eoOoKozpDpxPGhw8fhr+/PxwcHCCRSLBz506N64IgYNasWbC3t4eJiQl8fX1x+fJljT5paWkYNmwYLCwsYGlpidGjRyMrK0ujz5kzZ9C9e3fI5XI4Ojpi0aJFJWrZvn07XFxcIJfL4eHhgb1791a4FiIi0h0b8/JN2xUHqu4tG2DvuO4MVKQ1Og1V2dnZaNeuHVatWlXq9UWLFmH58uUIDQ1FZGQkTE1N4efnh9zcR38bGTZsGM6dO4f9+/dj9+7dOHz4MD744APxekZGBnr37g0nJydERUVh8eLFmDNnDtasWSP2OXbsGAIDAzF69GjExMQgICAAAQEBiIuLq1AtRESkO52crWCvkONZE3hSCTDVrzV+GtUJDc1l1VIb1Q0SQRBKW9NX7SQSCX777TcEBAQAKBoZcnBwwOTJkzFlyhQAgFKphK2tLdavX48hQ4bgwoULcHV1xcmTJ9GhQwcAQHh4OPr164dbt27BwcEBISEh+PTTT5GcnAxjY2MAwPTp07Fz505cvHgRADB48GBkZ2dj9+7dYj1dunSBp6cnQkNDy1VLeWRkZEChUECpVMLCwkIrnxsRET1S/PQfgFIXrFvWM8Ka4R3QydmqegujGq28v7/19nnRhIQEJCcnw9fXV2xTKBTo3LkzIiIiAAARERGwtLQUAxUA+Pr6QiqVIjIyUuzz4osvioEKAPz8/BAfH48HDx6IfR6/T3Gf4vuUp5bS5OXlISMjQ+OLiIiqTh93e4S87V3qCJSbgwUOTn6JgYqqjN6GquTkZACAra3mSeC2trbiteTkZNjYaB4dYGhoCCsrK40+pb3H4/coq8/j159VS2kWLFgAhUIhfjk6Oj7jpyYiouclMzRAgUotfi+VANP6uCAsuBusTI2f8kqi56O3oao2mDFjBpRKpfiVmJio65KIiGqtApUaC/ZewKj1J/EgpwAA4KCQY/tHXTHmpeaQcrsEqmJ6u6WCnZ0dACAlJQX29o+OFUhJSYGnp6fYJzU1VeN1hYWFSEtLE19vZ2eHlJQUjT7F3z+rz+PXn1VLaWQyGWQyLoIkotqpoufrVaXb6Q8xdlM0om+mi22+bWzx9aC2sKzH0SmqHno7UuXs7Aw7OzscOHBAbMvIyEBkZCR8fHwAAD4+PkhPT0dUVJTY5+DBg1Cr1ejcubPY5/DhwygoKBD77N+/H61bt0b9+vXFPo/fp7hP8X3KUwsRUV0SHpeEbgsPInDtcYzfEovAtcfRbeFBjWNgqsv+8ynot+xfMVAZGUgwc4Ar1o5oz0BF1UqnoSorKwuxsbGIjY0FULQgPDY2Fjdv3oREIsGECRMwf/587Nq1C2fPnsWIESPg4OAgPiHYpk0b9OnTB++//z5OnDiBo0ePIjg4GEOGDIGDgwMAYOjQoTA2Nsbo0aNx7tw5bN26FcuWLcOkSZPEOsaPH4/w8HAsWbIEFy9exJw5c3Dq1CkEBwcDQLlqISKqKypyvl5Vyi9U4/Ow83j/51NQPiz6i7OjlQl++agrRndzhkTC6T6qXjrdUuHvv//Gyy+/XKJ95MiRWL9+PQRBwOzZs7FmzRqkp6ejW7duWL16NVq1aiX2TUtLQ3BwMMLCwiCVSjFw4EAsX74cZmZmYp8zZ84gKCgIJ0+eRIMGDTB27FhMmzZN457bt2/HZ599huvXr6Nly5ZYtGgR+vXrJ14vTy3Pwi0ViKimU6kFdFt4sMzjYCQA7BRyHJn2SpVOBSam5SB4UzRO31KKbX3d7fDVwLZQmBhV2X2pbirv72+92aeqLmCoIqKaLuLqfQSuPf7Mfpvf7wKf5tZVUsMfZ5Pwya9nkJlbCAAwNpDiswFtMLyLE0enqEqU9/e33i5UJyIi/VPe8/XK268icgtU+HLvBfwccUNsc7Kuh1VDveHeSKH1+xFVFEMVERGVW3nP1ytvv/K6fi8bQZuice7Oo02UB7S1x4I3PGAu53Qf6QeGKiIiKrfi8/WSlbmlHgNTvKZKm7uW7zp9B//bcRZZef9N9xlKMcffDYGdHDndR3pFb7dUICIi/WMglWC2vysAlDi4uPj72f6uWlmknlugwowdZzFuc4wYqJo1NMXvQS9gaOcmDFSkdxiqiIioQorP17NTaE7x2SnkCHnbG33c7ct4ZfldSc1CwKqj2Hziptj2hlcjhAV3Qxt7PuhD+onTf0REVGF93O3Ry9WuSnZU3xF9C5/tjENOvgoAIDeS4vPX3DGofWOOTpFeY6giIqJKMZBKtLptQk5+IWb/fg7bo26JbS1tzLBqmDda2Zpr7T5EVYWhioiIdO5SSiaCNkbjcmqW2PZWh8aY+6o7TIwNdFgZUfkxVBERkc4IgoDtUbcw6/c45BaoAQD1jA0wP8Adb3g31nF1RBXDUEVERDqRnVeIz3bG4beY22Kbi505Vg71Rgsbs6e8kkg/MVQREVG1u5CUgaBN0bh2N1tsG9q5CWYNcIXciNN9VDMxVBERVQOVWqiSJ+VqGkEQsOnETcwNO4/8wqLpPjOZIb58wwOvtnPQcXVEz4ehioioioXHJWFu2HkkKR+dh2evkGO2v6tW9nSqKTJzCzBjx1nsPpMktrk5WGDVUG80bWCqw8qItIObfxIRVaHwuCSM2RCtEagAIFmZizEbohEel1TGK2uXuNtK+K84ohGoRvo44dcxXRmoqNbgSBURURVRqQXMDTtf6hl5AoqOdZkbdh69XO1q7VSgIAj4OeIGvthzAfmqouk+c7khFg1si74edWeUjuoGhioioipyIiGtxAjV4wQAScpcnEhI0+ommvpC+bAA0389gz/iksW2do0VWBHojSbW9XRYGVHVYKgiIqoiqZllB6rK9KtJTiemI3hzNBLTHopt777gjOl9XWBsyJUnVDsxVBERVREbc/mzO1WgX00gCAJ+PHodX/1xAQWqoolPhYkRvh7UDr1cbXVcHVHVYqgiIqoinZytYK+QI1mZW+q6KgkAO0XR9gq1QXpOPqZsP4O/LqSIbd5NLLE80AuN63O6j2o/jsESEVURA6kEs/1dARQFqMcVfz/b31Xni9RVagERV+/j99jbiLh6Hyp1aRHw6aJuPEC/Zf9qBKoPezTD1g99GKiozuBIFRFRFerjbo+Qt71L7FNlpyf7VD3vHlpqtYA1/17D4n3xYhirX88I37zliZddbKqsbiJ9JBEEoeJ/JaFKycjIgEKhgFKphIWFha7LIaJqpI87qhfvofXkL4HiqkLe9n5qsErLzsfkbbE4FH9XbOvYtD6WB3rBXmGi/YKJdKS8v785UkVEVA0MpBK92jbheffQOpGQhnGbY5CcUTTCJZEAQS+1wATfljA04MoSqpsYqoiI6qDK7qGlVgtY/fcVfLP/EoqXXlmbGuPbwZ54sVXDKq6aSL8xVBER1UGV2UPrbmYeJm2Lxb+X74ltPs2ssWyIJ2wsas+2EESVxVBFRFQHVXQPrWNX7mH81ljczcwDUDTdN+6VlhjXs6XO14YR6QuGKiKiOqi8e2i1d6qPb/dfwvKDl1H8WFNDcxmWDfZE1xYNqrNkIr3H1YRERHVQefbQmtCzJUb+eALLDjwKVN1bNsDecd0ZqIhKwVBFRFRHFe+hZafQnAq0U8gxtmcLLP4zHhHX7gMApBJgSu9W+GlUJzQ0l+miXCK9x+k/IqI6rI+7PXq52ol7aFmbynDs6j2sOHhFHJ2ytZBh+RAvdG6mP1tCEOkjhioiojqueA+tJOVDjN8cixPX08RrL7VuiCWD2sHajKNTRM/CUEVERDh0MRWTtsXiQU4BgKKgNdWvNT7o3gxSPt1HVC4MVUREdViBSo2v/4zHd/9cE9scFHKsGOqF9k5WOqyMqOZhqCIiqqNupz/E2E3RiL6ZLrb5trHB4jfbob6pse4KI6qhGKqIiOqg/edTMGX7aSgfFk33GUolmN7XBaO7OUMi4XQfUWUwVBER1SH5hWp89cdF/Hg0QWxrXN8EK4d6w9PRUneFEdUCDFVERHVEYloOgjdF4/QtpdjWx80OC99sC4WJkQ4rI6odGKqIiOqA8LgkTP3lDDJzCwEAxgZSfNq/DUb4OHG6j0hLGKqIiGqx3AIVFuy9gJ8ibohtTtb1sDLQGx6NFTqsjKj2YagiIqqlrt/LRtCmaJy7kyG29W9rj6/e8IC5nNN9RNrGUEVEVAuFnb6DGTvOIivvv+k+Qylm+7tiaKcmnO4jqiIMVUREtUhugQqf7z6PTZE3xbZmDUyxcqg3XB0sdFgZUe3HUEVEVEtcvZuFoI3RuJicKbYFeDpg/useMJPxj3uiqsb/y4iIaoHfYm7h09/ikJOvAgDIjaT4/FV3DOrQmNN9RNWEoYqIqAZ7mK/C7F1x2HbqltjWwsYMq4d5o5WtuQ4rI6p7GKqIiGqoyymZ+HhjNC6nZoltg9o3xtzX3FDPmH+8E1U3/l9HRFTDCIKA7VG3MOv3OOQWqAEAJkYG+OJ1d7zh3VjH1RHVXQxVREQ1SHZeIWbujMOOmNtim4udOVYO9UYLGzMdVkZEDFVERDXEhaQMBG+KxtW72WJbYCdHzPZ3g9zIQIeVEREASCvzokOHDmm7DiIiKoMgCNgUeRMBq46KgcrU2ADLhnhiwRttGaiI9ESlRqr69OmDxo0bY9SoURg5ciQcHR21XRcREQHIzC3A/36LQ9jpO2Kbq70FVg3zhnMDUx1WRkRPqtRI1e3btxEcHIxffvkFzZo1g5+fH7Zt24b8/Hxt10dEVGfF3VbCf8URjUA1wscJOz7uykBFpIckgiAIz/MG0dHRWLduHTZv3gwAGDp0KEaPHo127dpppcDaJCMjAwqFAkqlEhYWPC6CqLqo1AJOJKQhNTMXNuZydHK2goFUfzfEFAQB/3f8BubvvoB8VdHTfeYyQyx8sy36edjruDqiuqe8v7+fO1QBwJ07d7BmzRp89dVXMDQ0RG5uLnx8fBAaGgo3N7fnfftag6GKqPqFxyVhbth5JClzxTZ7hRyz/V3Rx13/AoryYQFm7DiDvWeTxba2jRVYGeiNJtb1dFgZUd1V3t/flZr+A4CCggL88ssv6NevH5ycnLBv3z6sXLkSKSkpuHLlCpycnDBo0KDKvj0R0XMLj0vCmA3RGoEKAJKVuRizIRrhcUk6qqx0pxPTMWDFvxqB6t0XnLH9Ix8GKqIaoFIjVWPHjsXmzZshCAKGDx+O9957D+7u7hp9kpOT4eDgALVarbViazqOVBFVH5VaQLeFB0sEqmISAHYKOY5Me0XnU4GCIODHo9fx1R8XUKAq+iPZQm6Irwe1Q283O53WRkTl//1dqaf/zp8/jxUrVuCNN96ATCYrtU+DBg249QIR6cyJhLQyAxUACACSlLk4kZAGn+bW1VfYE9Jz8jH1lzPYfz5FbPNqYokVgV5oXJ+jU0Q1SYVDVUFBAZycnNClS5cyAxUAGBoaokePHs9VHBFRZaVmlh2oKtOvKkTffICxm2JwO/2h2Pbhi80wxa81jAwqvTqDiHSkwv/XGhkZ4ddff62KWoiItMbGXK7VftqkVgv47p+reCs0QgxU9esZ4cd3OmBGvzYMVEQ1VKX+zw0ICMDOnTu1XAoRkfZ0craCvUKOslZLSVD0FGAnZ6squb9KLSDi6n38HnsbEVfvQ6UuWiuVlp2P934+hQV/XEThf20dm9bH3vHd8YqLbZXUQkTVo1Jrqlq2bInPP/8cR48eRfv27WFqqrkJ3bhx47RSHBFRZRlIJZjt74oxG6IhQdEaqmLFQWu2v2uVLFIvaxuHYZ2bYMPxm0jOeNT+8UvNMalXKxhydIqoxqvU03/Ozs5lv6FEgmvXrj1XUbUVn/4jqn7VvU9V8TYOz/qD1drUGN8M9kSPVg21XgMRaVeVPv2XkJBQ6cKIiKpTH3d79HK1q5Yd1VVqAXPDzj8zUHV2tsLyQC/YWlT/ei4iqjqVClVERDWJgVRSLdsmPGsbh2LjXmnJQEVUC1U6VN26dQu7du3CzZs3Sxyk/M033zx3YURENU15t2e4l51XxZUQkS5UamXkgQMH0Lp1a4SEhGDJkiU4dOgQ1q1bhx9//BGxsbFaK06lUmHmzJlwdnaGiYkJmjdvjnnz5uHxZWCCIGDWrFmwt7eHiYkJfH19cfnyZY33SUtLw7Bhw2BhYQFLS0uMHj0aWVlZGn3OnDmD7t27Qy6Xw9HREYsWLSpRz/bt2+Hi4gK5XA4PDw/s3btXaz8rEdV8+ryNAxFVvUqFqhkzZmDKlCk4e/Ys5HI5fv31VyQmJqJHjx5aPe9v4cKFCAkJwcqVK3HhwgUsXLgQixYtwooVK8Q+ixYtwvLlyxEaGorIyEiYmprCz88PubmP/sY4bNgwnDt3Dvv378fu3btx+PBhfPDBB+L1jIwM9O7dG05OToiKisLixYsxZ84crFmzRuxz7NgxBAYGYvTo0YiJiUFAQAACAgIQFxentZ+XiGq2ApUaT1uqVdXbOBCRblXq6T9zc3PExsaiefPmqF+/Po4cOQI3NzecPn0ar732Gq5fv66V4gYMGABbW1v88MMPYtvAgQNhYmKCDRs2QBAEODg4YPLkyZgyZQoAQKlUwtbWFuvXr8eQIUNw4cIFuLq64uTJk+jQoQMAIDw8HP369cOtW7fg4OCAkJAQfPrpp0hOToaxsTEAYPr06di5cycuXrwIABg8eDCys7Oxe/dusZYuXbrA09MToaGh5fp5+PQfUe1UqFJj6V+XservKyjrT9TirBXytneVPHVIRFWnvL+/KzVSZWpqKq6jsre3x9WrV8Vr9+7dq8xblqpr1644cOAALl26BAA4ffo0jhw5gr59+wIoegoxOTkZvr6+4msUCgU6d+6MiIgIAEBERAQsLS3FQAUAvr6+kEqliIyMFPu8+OKLYqACAD8/P8THx+PBgwdin8fvU9yn+D6lycvLQ0ZGhsYXEdUuycpcDP0+EisPPQpUbg4WsDHXPMbLTiFnoCKq5Sq1UL1Lly44cuQI2rRpg379+mHy5Mk4e/YsduzYgS5dumituOnTpyMjIwMuLi4wMDCASqXCF198gWHDhgEAkpOTAQC2tpq7ENva2orXkpOTYWNjo3Hd0NAQVlZWGn2e3Hur+D2Tk5NRv359JCcnP/U+pVmwYAHmzp1b0R+biGqIv+NTMWnbaaRlF/0l00AqwZTerfHhi80gANWyjQMR6Y9KhapvvvlGXOg9d+5cZGVlYevWrWjZsqVWn/zbtm0bNm7ciE2bNsHNzQ2xsbGYMGECHBwcMHLkSK3dp6rMmDEDkyZNEr/PyMiAo6OjDisiIm0oUKmx5M9LCP3n0Si9g0KOFUO90N7p0Xqp6tjGgYj0R6VCVbNmzcR/NjU1LfeaooqaOnUqpk+fjiFDhgAAPDw8cOPGDSxYsAAjR46EnZ0dACAlJQX29o+G1FNSUuDp6QkAsLOzQ2pqqsb7FhYWIi0tTXy9nZ0dUlJSNPoUf/+sPsXXSyOTySCTycq8TkQ1z+30hxi3OQZRNx6Ibb5tbLD4zXaob2r8lFcSUW2n14dN5eTkQCrVLNHAwABqtRpA0XE5dnZ2OHDggHg9IyMDkZGR8PHxAQD4+PggPT0dUVFRYp+DBw9CrVajc+fOYp/Dhw+joKBA7LN//360bt0a9evXF/s8fp/iPsX3IaLa76/zKei37F8xUBlKJfisfxusHdGBgYqIyj9SVb9+fUgk5VsPkJaWVumCHufv748vvvgCTZo0gZubG2JiYvDNN9/g3XffBVB0zuCECRMwf/58tGzZEs7Ozpg5cyYcHBwQEBAAAGjTpg369OmD999/H6GhoSgoKEBwcDCGDBkCBwcHAMDQoUMxd+5cjB49GtOmTUNcXByWLVuGb7/9Vqxl/Pjx6NGjB5YsWYL+/ftjy5YtOHXqlMa2C0RUO+UXqrEo/CK+P/LoiK5GliZYOdQLXk3q67AyItIn5d5S4aeffir3m2prvVNmZiZmzpyJ3377DampqXBwcEBgYCBmzZolPqknCAJmz56NNWvWID09Hd26dcPq1avRqlUr8X3S0tIQHByMsLAwSKVSDBw4EMuXL4eZmZnY58yZMwgKCsLJkyfRoEEDjB07FtOmTdOoZ/v27fjss89w/fp1tGzZEosWLUK/fv3K/fNwSwWimicxLQfBm2NwOjFdbPNzs8Wige2gqGeku8KIqNqU9/d3pfaposphqCKqWcLjkjD1lzPIzC0EABgbSPG/fi4Y2bVpuUfuiajmK+/v7+c+UDk3N7fE2X8MDERUk+UVqvDlngv4KeKG2NbEqh5WDfWGR2OFDisjIn1WqVCVnZ2NadOmYdu2bbh//36J6yqV6rkLIyLShev3shG8ORpxtx9t1tu/rT0WvOEBCzmn+4iobJV6+u+TTz7BwYMHERISAplMhu+//x5z586Fg4MDfv75Z23XSERULXafuYMBK46IgcrYUIr5Ae5YGejFQEVEz1SpkaqwsDD8/PPPeOmllzBq1Ch0794dLVq0gJOTEzZu3CjueE5EVBPkFqjw+e7z2BR5U2xzbmCKlUO94ObA6T4iKp9Khaq0tDRxA1ALCwtxC4Vu3bphzJgx2quOiKiKXb2bhaCN0biYnCm2vebpgC9e94CZ7LmXnRJRHVKp6b9mzZohIaFovxYXFxds27YNQNEIlqWlpdaKIyKqSjtjbsN/xRExUMkMpVg40ANLB3syUBFRhVXqT41Ro0bh9OnT6NGjB6ZPnw5/f3+sXLkSBQUFWj37j4ioKjzMV2HOrnPYeipRbGthY4ZVQ73R2s5ch5URUU2mlX2qbty4gaioKLRo0QJt27bVRl21EvepItK9yymZCNoUjUspWWLbQO/GmBfghnrGHJ0iopLK+/u7QtN/ERER2L17t0Zb8YL1jz76CCtXrkReXl7lKiYiqmLbTyXi1ZVHxUBlYmSArwe1w5K32jFQEdFzq1Co+vzzz3Hu3Dnx+7Nnz2L06NHw9fXFjBkzEBYWhgULFmi9SCKi55GdV4hJ22Ix9ZczeFhQtI9ea1tzhI19AW+2b6zj6oiotqjQX81iY2Mxb9488fstW7agc+fOWLt2LQCgcePGmD17NubMmaPVIomIKuticgaCNkbj6t1ssW1IR0fM9neDibGBDisjotqmQqHqwYMHsLW1Fb//559/0LdvX/H7jh07IjExsbSXEhFVK0EQsOVkIubsOoe8QjUAwNTYAF++4YHXPBvpuDoiqo0qNP1na2srbqWQn5+P6OhodOnSRbyemZkJIyPuOkxEupWZW4BxW2IxY8dZMVC1sbdA2NhuDFREVGUqNFLVr18/TJ8+HQsXLsTOnTtRr149dO/eXbx+5swZNG/eXOtFEhGVV9xtJYI3ReP6/RyxbXgXJ3zavw3kRpzuI6KqU6FQNW/ePLzxxhvo0aMHzMzM8NNPP8HY2Fi8/uOPP6J3795aL5KI6FkEQcCG4zcwb/cF5KuKRqfMZYb4amBb9G9rr+PqiKguqNQ+VUqlEmZmZjAw0PxbX1paGszMzDSCFj3CfaqIqkZGbgGm/3oGe88mi20ejRRYOdQLTtamOqyMiGqD8v7+rtTGLApF6QeMWllZVebtiIgq7cytdARtikZi2kOx7Z2uTTGjnwtkhpzuI6Lqw93uiKhGEgQB645ex4I/LqBAVTTgbiE3xOJB7eDnZqfj6oioLmKoIqIaR5lTgKm/nMaf51PENk9HS6wI9IKjVT0dVkZEdRlDFRHVKNE3H2DsphjcTn803fd+d2dM9XOBsWGFdokhItIqhioiqhHUagHfH7mGReHxKFQXTfdZ1jPCkkHt0LON7TNeTURU9RiqiEjvPcjOx+Ttp3HwYqrY1sGpPpYHesHB0kSHlRERPcJQRUR67dT1NIzdHIMkZa7Y9vFLzTGxVysYGXC6j4j0B0MVEekltVpA6OGrWPLnJaj+m+6zNjXGN4M90aNVQx1XR0RUEkMVEemde1l5mLTtNA5fuiu2dWlmhWVDvGBrIddhZUREZWOoIiK9cvzafYzbHIPUzDwAgEQCjH2lJcb3bAkDqUTH1RERlY2hioj0gkotYNWhK1j61yX8N9uHBmYyLBviiRdaNNBtcURE5cBQRUQ6l5qZi4lbY3H0yn2xrVuLBvh2sCcamst0WBkRUfkxVBGRTh29cg/jt8TiXlbRdJ9UAkz0bYWPX27B6T4iqlEYqohIJwpVaiw/cBkrDl2B8N90n62FDMuGeKFLM2vdFkdEVAkMVURU7VIycjF2cwxOJKSJbT1aNcQ3b7WDtRmn+4ioZmKoIqJq9Xd8KiZtO4207HwAgIFUgim9W+PDF5tByuk+IqrBGKqIqFoUqtRYsv8SQv6+KrbZK+RYEeiFDk2tdFgZEZF2MFQRUZW7k/4Q4zbH4NSNB2JbTxcbfD2oHeqbGuuwMiIi7WGoIqIqdeBCCiZvP430nAIAgKFUgul9XTC6mzMkkrKn+1RqAScS0pCamQsbczk6OVvxaUAi0msMVURUJfIL1Vi87yLW/psgtjWyNMHKoV7walL/qa8Nj0vC3LDzGoco2yvkmO3vij7u9lVWMxHR8+AR70SkdYlpOXjruwiNQOXnZou947qXK1CN2RCtEagAIFmZizEbohEel1QlNRMRPS+OVBGRVu07l4yp208jI7cQAGBsIMX/+rlgZNemT53uA4qm/OaGnYdQyjUBgATA3LDz6OVqx6lAItI7DFVEpBV5hSos2HsR649dF9uaWNXDqqHe8GisKNd7nEhIKzFC9TgBQJIyFycS0uDTnBuEEpF+Yagioud24342gjfF4OxtpdjWv609FrzhAQu5UbnfJzWz7EBVmX5ERNWJoYqInsueM0mY/usZZOb9N91nKMWsAa4Y1rnJM6f7nmRjLtdqPyKi6sRQRUSVklugwvw957Hh+E2xrVkDU6wc6g1XB4tKvWcnZyvYK+RIVuaWuq5KAsBOUbS9AsBtF4hIvzBUEVGFXbubhaBNMbiQlCG2BXg6YP7rHjCTVf6PFQOpBLP9XTFmQzQkgEawKo5Ks/1dYSCVcNsFItI73FKBiCrk99jb8F9xRAxUciMpFg70wLeDPZ8rUBXr426PkLe9YafQnOKzU8gR8rY3+rjbc9sFItJLHKkionJ5mK/C3LBz2HIyUWxrYWOGVUO90drOXKv36uNuj16udqVO7XHbBSLSVwxVRPRMV1IzEbQxBvEpmWLbm+0b4/PX3FDPuGr+GDGQSkrdNoHbLhCRvmKoIqKn+iXqFmbujMPDAhUAwMTIAPMD3DGwfWOd1MNtF4hIXzFUEWlZbXkiLSe/EDN3nsOv0bfEtta25lg1zAstbLQ73VcR3HaBiPQVQxWRFtWWJ9LikzPx8cYoXL2bLbYFdnLEbH83yI0MdFhZxbddICKqLnz6j0hLasMTaYIgYMuJm3h15RExUJkaG2DZEE8seKOtzgMV8GjbBeDRNgvFntx2gYioOjFUEWnBs55IA4qeSFOpS+uhH7LyCjFhayym7ziLvEI1AMDV3gJhY7vhNc9GOq5OU3m2XSAiqm6c/iPSAn18Iq0ia7vO3VEieFMMEu49mu4b3sUJn/ZvoxejU6V52rYLRES6wFBFpAX69kRaedd2CYKADZE3MW/3eeT/NzplLjPEVwPbon9b/R/tKWvbBSIiXeD0H5EW6NMTaeVd25WRW4DgTTGYuTNODFQejRTYPa5bjQhURET6hiNVRFqgL0+klXe3cVsLOcZvicXNtBzx+jtdm2JGPxfIDPVzuo+ISN9xpIpIC/TlibTyru16MzRCDFQWckN8N7w95rzqxkBFRPQcGKqItEQfnkgr75qt4qcQPR0tsXd8d/i52VVlWUREdQKn/4i0SNdPpFVkzdYHLzbDVL/WMDLg362IiLSBoYpIy3T5RNqz1nYBgEQCrBneHr1cOTpFRKRN/CsqUS3y+NqusnwR4F5lgUqlFhBx9T5+j72NiKv39XqzUyIibeNIFVEt08fdHpN7t8I3+y/h8UxjKjPAooFt0b+tQ5Xct7ace0hEVFkMVUS1iFotIPTwVXz712UxUJnKDDD25ZZ4/8VmVba2q3hvrCfHpYr3xuLRMURUFzBUEdUS97LyMGnbaRy+dFds6+xsheWBXrC1qLpNR8u7N1YvVzseIUNEtRpDFVEFVOQ8vep0/Np9jNscg9TMPABFi9HHvtIS415pAcMqfrpPH889JCLSBb1fqH779m28/fbbsLa2homJCTw8PHDq1CnxuiAImDVrFuzt7WFiYgJfX19cvnxZ4z3S0tIwbNgwWFhYwNLSEqNHj0ZWVpZGnzNnzqB79+6Qy+VwdHTEokWLStSyfft2uLi4QC6Xw8PDA3v37q2aH5r0UnhcErotPIjAtccxfkssAtceR7eFB8VjX3RBpRaw7K/LGLr2uBioGpjJsGF0Z0zq1arKAxWgf+ceEhHpil6HqgcPHuCFF16AkZER/vjjD5w/fx5LlixB/fr1xT6LFi3C8uXLERoaisjISJiamsLPzw+5uY/+AB82bBjOnTuH/fv3Y/fu3Th8+DA++OAD8XpGRgZ69+4NJycnREVFYfHixZgzZw7WrFkj9jl27BgCAwMxevRoxMTEICAgAAEBAYiLi6ueD4N0qrzn6VWn1MxcjPgxEt/+9WhB+gstrLF3fDe80KJBtdWhT+ceEhHpkkQQBL195nn69Ok4evQo/v3331KvC4IABwcHTJ48GVOmTAEAKJVK2NraYv369RgyZAguXLgAV1dXnDx5Eh06dAAAhIeHo1+/frh16xYcHBwQEhKCTz/9FMnJyTA2NhbvvXPnTly8eBEAMHjwYGRnZ2P37t3i/bt06QJPT0+EhoaW6+fJyMiAQqGAUqmEhYVFpT8Xql4qtYBuCw+WOcVVfK7fkWmvVNtU4NEr9zB+SyzuZRWNTkklwATfVgh6uUW1T0cWfz7POvewOj8fIiJtKu/vb70eqdq1axc6dOiAQYMGwcbGBl5eXli7dq14PSEhAcnJyfD19RXbFAoFOnfujIiICABAREQELC0txUAFAL6+vpBKpYiMjBT7vPjii2KgAgA/Pz/Ex8fjwYMHYp/H71Pcp/g+VHtVZM1QVStUqbHkz3i8/UOkGKhszGXY9H4XjOvZUiehRV/OPSQi0jW9DlXXrl1DSEgIWrZsiX379mHMmDEYN24cfvrpJwBAcnIyAMDW1lbjdba2tuK15ORk2NjYaFw3NDSElZWVRp/S3uPxe5TVp/h6afLy8pCRkaHxRTWPvqwZSlbmYuj3kVhx8AqKx5dfbNUQe8d3R5dmul0Arg/nHhIR6ZpeP/2nVqvRoUMHfPnllwAALy8vxMXFITQ0FCNHjtRxdc+2YMECzJ07V9dl0HPShzVDf8enYtK200jLzgdQNDo0qVcrjOnRHFI9GQHS9bmHRES6ptcjVfb29nB11Txyo02bNrh58yYAwM6u6KiNlJQUjT4pKSniNTs7O6SmpmpcLywsRFpamkaf0t7j8XuU1af4emlmzJgBpVIpfiUmJj77hya9U3yeXlnRQIKincM7OVtp/d4FKjUWhl/EO+tOioHKXiHHlg+6IOjlFnoTqIoVn3v4mmcj+DS3ZqAiojpFr0PVCy+8gPj4eI22S5cuwcnJCQDg7OwMOzs7HDhwQLyekZGByMhI+Pj4AAB8fHyQnp6OqKgosc/BgwehVqvRuXNnsc/hw4dRUFAg9tm/fz9at24tPmno4+OjcZ/iPsX3KY1MJoOFhYXGF9U8ulozdCf9IYasOY6Qv6+Kba+42GDvuO7o2FT7AY6IiJ6PXoeqiRMn4vjx4/jyyy9x5coVbNq0CWvWrEFQUBAAQCKRYMKECZg/fz527dqFs2fPYsSIEXBwcEBAQACAopGtPn364P3338eJEydw9OhRBAcHY8iQIXBwKDoDbejQoTA2Nsbo0aNx7tw5bN26FcuWLcOkSZPEWsaPH4/w8HAsWbIEFy9exJw5c3Dq1CkEBwdX++dC1a+61wwduJCCfsv/RdSNogclDKUSfNqvDb4f0QH1TY2f8WoiItIJQc+FhYUJ7u7ugkwmE1xcXIQ1a9ZoXFer1cLMmTMFW1tbQSaTCT179hTi4+M1+ty/f18IDAwUzMzMBAsLC2HUqFFCZmamRp/Tp08L3bp1E2QymdCoUSPhq6++KlHLtm3bhFatWgnGxsaCm5ubsGfPngr9LEqlUgAgKJXKCr2O9EehSi0cu3JP2BlzSzh25Z5QqFJr9f3zClTCvLBzgtO03eJX1wUHhKgbaVq9DxERlV95f3/r9T5VtQ33qaKnSUzLwdjNMYhNTBfbervaYvGb7aCoZyS26etROUREtVV5f3/r9dN/RHXFvnPJmLr9NDJyCwEARgYS/K9fG7zTtSkkkkeBKTwuCXPDzmvsm2WvkGO2v2u5piCfDGTtneoj6sYDBjQiIi1gqCIqQ3WMCOUVqrBg70WsP3ZdbGtiVQ8rh3qhbWNLjb7FR+U8ObRcfFTOs9Z2lRbIpBKIR9wAFQtoRESkiaGKqBTPOyJUHjfuZyN4UwzO3laKbf087PDVwLawkBtp9FWpBcwNO1/qMTACip5CnBt2Hr1c7UoNfmUFMvUTDeUNaEREVJJeP/1HpAvVcXjynjNJGLD8iBiojA2lmBfgjlVDvUsEKuD5jsp5WiAr7X2AooCmejJxERHRUzFUET3mWSNCwPMFjtwCFT7beRZBm6KRmVe0fsq5gSl++7grhndx0lg/9bjnOSrnWYHsSdV5liERUW3C6T+ix1RkRMinecXO27t2NwtBm2JwIenRGZCvtnPAl294wEz29P8Vn+eonMqeSVjVZxkSEdU2DFVEj6mqw5N/j72N/+04i+x8FQBAZijF3FfdMLijY5mjU48rPionWZlb6iiaBEUbkZZ2VE5lzySsyrMMiYhqI07/ET1G24cnP8xXYfqvZzB+S6wYqJo3NMXvwS9gSKcm5QpUwPMdldPJ2QqW9Uqu0ypLVZ5lSERUmzFUET1Gm4cnX0nNRMCqo9hy8tFB2gO9GyNsbDe42FV889fqOCqnKs8yJCKq7Tj9R/SY4hGhMRuiIQE0ptoqEjh+jbqFz3bG4WFB0eiUiZEB5gW44832jZ+rvj7u9ujlaleh/bNOJKQhPaegzOuPs+M+VURElcZQRfSE4hGhJ/epKk/gyMkvxGc747Aj+rbY1tLGDKuHeaOlrblW6jOQSiq0SL6867+CX26Oib1ac4SKiKiSGKqISlGZEaH45EyMXHcCyU88PZiZW4Crd7O0Fqoqqrzrv15o0ZCBiojoOTBUEZWhvCNCgiBg26lEfLYzDgWqks/mpWTk6XSX8ud5cpCIiMqPC9WJnkNWXiEmbo3FtF/PlhqoAN3vUv48Tw4SEVH5MVQRVdL5Oxl4dcUR7Iy988y+ut6lvDqeHCQiqus4/UdUQYIgYGPkTXy++zzyC9UAijbzzPvvn59Gl7uUV2adGBERlR9DFVEFZOQWYMaOs9hz5tGhyu6NLPBet2aYsDX2ma/X9S7lFX1ykIiIyo+hiqic4m4rEbQpGjfu54ht73Rtihn9XGAolWJh+EUuBiciqsO4poroGQRBwPqjCXhj9TExUFnIDRH6tjfmvOoGmaEBF4MTERFDFdHTKHMK8NGGKMwJO498VdGaqXaOltgzrnuJxd1cDE5EVLdx+o+oDDE3H2Ds5hjcevBQbHu/uzOm+rnA2LD0v49wMTgRUd3FUEX0BEEQ8P2/CVgYfhGF/+0rZVnPCF+/2Q6+rrbPfD0XgxMR1U0MVUSPeZCdjynbT+PAxVSxrYNTfSwP9IKDpYkOKyMiIn3HUEX0n1PX0zBucwzuPHZ235iXmmNSr1YwMuDyQyIiejqGKqrz1GoBoYevYsmfl8RjZKxMjfHNW+3wUmsbHVdHREQ1BUMV1Wn3s/Iwadtp/HPprtjWydkKy4d4lXiKj4iI6GkYqqjOOn7tPsZviUFKRh4AQCIBxr7cAuN6toQhp/uIiKiCGKqozlGpBaw6dAVL/7qE/2b70MBMhqWDPdGtZQPdFkdERDUWQxXVKamZuZi4NRZHr9wX27o2t8bSIZ46P5ePiIhqNoYqqjOOXrmH8VticS+raLpPKgEm+LZC0MstuDknERE9N4YqqvVUagHLDlzGioOXIfw33WdjLsOyIV7cpJOIiLSGoYpqtZSMXIzbHIPIhDSx7cVWDfHNW+3QwEymw8qIiKi2YaiiWuufS3cxaWss7mfnAyg6PmZy71b46MXmkHK6j4iItIyhimqdQpUaS/ZfQsjfV8U2e4UcywO90LGplQ4rIyKi2oyhimqVO+kPMW5zDE7deCC2veJigyWD2qG+qbEOKyMiotqOoYpqjYMXUzBp22mk5xQAAAylEkzr44LR3Zw53UdERFWOoYpqvAKVGovCL2LtvwliWyNLE6wY6gXvJvV1WBkREdUlDFVUoyWm5WDs5hjEJqaLbb1dbbH4zXZQ1DPSXWFERFTnMFRRjbXvXDKmbj+NjNxCAICRgQT/69cG73RtComE031ERFS9GKqoxskrVOGrPy5i3dHrYlsTq3pYOdQLbRtb6qwuIiKq2xiqqEa5cT8bwZticPa2Umzr52GHrwa2hYWc031ERKQ7DFV1hEot4ERCGlIzc2FjLkcnZ6sad97dnjNJmP7rGWTmFU33GRtKMXOAK97u3ITTfUREpHMMVXVAeFwS5oadR5IyV2yzV8gx298VfdztdVhZ+eQWqDB/z3lsOH5TbHNuYIqVQ73g5qDQYWVERESPSHVdAFWt8LgkjNkQrRGoACBZmYsxG6IRHpeko8rKJ+FeNt5YfUwjUL3azgFhY7sxUBERkV7hSFUtplILmBt2HkIp1wQAEgBzw86jl6udXk4F/h57G//bcRbZ+SoAgMxQirmvumFwR0dO9xERkd5hqKrFTiSklRihepwAIEmZixMJafBpbl19hT1DboEKc8POYfOJRLGteUNTrBrmDRc7Cx1WRkREVDaGqlosNbPsQFWZftXhSmomgjbGID4lU2x7w7sR5r3mDlMZ/3MlIiL9xd9StZiNuVyr/arar1G38NnOODwsKJruMzEywOevuWFQB0cdV0ZERPRsDFW1WCdnK9gr5EhW5pa6rkoCwE5RtL2CLuXkF2LW7+fwS9Qtsa2VrRlWDfVGS1tzHVZGRERUfnz6rxYzkEow298VQFGAelzx97P9XXW6SD0+OROvrjyqEagGd3DE70HdGKiIiKhGYaiq5fq42yPkbW/YKTSn+OwUcoS87a2zfaoEQcDWkzfx6sojuJKaBQCoZ2yApYM9sfDNtjAxNtBJXURERJXF6b86oI+7PXq52unFjuoqtYB/4u9i1d9XEHXjgdjext4Cq4Z6oVlDs2qviYiISBsYquoIA6lE59smhMcl4bOdcbiXla/R/mLLBlgzogPkRhydIiKimovTf1Qt/jh7Bx9tiC4RqADg38v38Hd8qg6qIiIi0h6GKqpy6Tn5mLjt9FP7zA07D5W6tGcUiYiIagaGKqpSZ28p4bf0MHIL1GX2eXxndyIiopqKa6qoSgiCgJ+OXceXey8iX1V2oHqcPu3sTkREVFEMVaR1ypwCfPLraew7l1Kh1+nLzu5ERESVwek/0qrYxHT0X/GvRqB694WmsLOQldiAtJgEgL0e7OxORET0PDhSRVohCAJ+OJKAr/64iML/FpwrTIzw9aB26OVqi07OVhizIRoSQOPIHH3Z2Z2IiOh5caSKnlt6Tj7e//kU5u+5IAYq7yaW2Du+O3q52gLQ353diYiItIUjVfRcom6kYeymGNxRPlpk/mGPZpjSuzWMDDQzuz7t7E5ERKRtDFVUKWq1gO8OX8PXf8aL+0tZmRpjyVvt8HJrmzJfpw87uxMREVUFhiqqsPtZeZi8/TT+jr8rtnVqaoXlgV4lpveIiIjqCoYqqpDIa/cxbksMUjLyAAASCRD8cguM79kShgZcokdERHVXjfot+NVXX0EikWDChAliW25uLoKCgmBtbQ0zMzMMHDgQKSma+yPdvHkT/fv3R7169WBjY4OpU6eisLBQo8/ff/8Nb29vyGQytGjRAuvXry9x/1WrVqFp06aQy+Xo3LkzTpw4URU/pl5SqQWsOHAZgWuPi4GqgZkxfn63Eyb3bq3VQKVSC4i4eh+/x95GxNX7PL6GiIhqhBozUnXy5El89913aNu2rUb7xIkTsWfPHmzfvh0KhQLBwcF44403cPToUQCASqVC//79YWdnh2PHjiEpKQkjRoyAkZERvvzySwBAQkIC+vfvj48++ggbN27EgQMH8N5778He3h5+fn4AgK1bt2LSpEkIDQ1F586dsXTpUvj5+SE+Ph42NmWvIaoN7mbmYeLWWBy5ck9s82lmjWVDPGFjod3pvvC4JMwNO4+kxxa+2yvkmO3vyicEiYhIr0kEQdD7YYCsrCx4e3tj9erVmD9/Pjw9PbF06VIolUo0bNgQmzZtwptvvgkAuHjxItq0aYOIiAh06dIFf/zxBwYMGIA7d+7A1rbo8f7Q0FBMmzYNd+/ehbGxMaZNm4Y9e/YgLi5OvOeQIUOQnp6O8PBwAEDnzp3RsWNHrFy5EgCgVqvh6OiIsWPHYvr06eX6OTIyMqBQKKBUKmFhYaGVz0alFqr0abpjV+5h/NZY3M0sGp2SSoDxPVsh+JUWWn9qLzwuCWM2ROPJ/yCL78KtF4iISBfK+/u7Rkz/BQUFoX///vD19dVoj4qKQkFBgUa7i4sLmjRpgoiICABAREQEPDw8xEAFAH5+fsjIyMC5c+fEPk++t5+fn/ge+fn5iIqK0ugjlUrh6+sr9tGF8LgkdFt4EIFrj2P8llgErj2ObgsPIjwu6bnfW6UW8M3+Sxj2Q6QYqBqay7DxvS4Y79tS64FKpRYwN+x8iUAFPNosdG7YeU4FEhGR3tL76b8tW7YgOjoaJ0+eLHEtOTkZxsbGsLS01Gi3tbVFcnKy2OfxQFV8vfja0/pkZGTg4cOHePDgAVQqVal9Ll68WGbteXl5yMvLE7/PyMh4xk9bfmWN6iQrczFmQ/RzjeqkZORi/JYYHL+WJrZ1b9kA3w72RAMz2XNUXbYTCWkaU35PEgAkKXNxIiGNWzIQEZFe0uuRqsTERIwfPx4bN26EXF7zHtVfsGABFAqF+OXo6KiV963KUZ3Dl+6i37J/xUAllQBT/Vrjp1GdqixQAUBqZtmBqjL9iIiIqpteh6qoqCikpqbC29sbhoaGMDQ0xD///IPly5fD0NAQtra2yM/PR3p6usbrUlJSYGdnBwCws7Mr8TRg8ffP6mNhYQETExM0aNAABgYGpfYpfo/SzJgxA0qlUvxKTEys1OfwpIqM6pRXoUqNxfsuYuS6E7ifnQ8AsLOQY8sHPgh6uQWkVbzruY15+UJzefsRERFVN70OVT179sTZs2cRGxsrfnXo0AHDhg0T/9nIyAgHDhwQXxMfH4+bN2/Cx8cHAODj44OzZ88iNTVV7LN//35YWFjA1dVV7PP4exT3KX4PY2NjtG/fXqOPWq3GgQMHxD6lkclksLCw0PjSBm2P6iQpHyJw7XGsOnQVxY8tvNy6IfaO745OzlaVLbNCOjlbwV4hR1nRTYKipwCrqx4iIqKK0us1Vebm5nB3d9doMzU1hbW1tdg+evRoTJo0CVZWVrCwsMDYsWPh4+ODLl26AAB69+4NV1dXDB8+HIsWLUJycjI+++wzBAUFQSYrms766KOPsHLlSnzyySd49913cfDgQWzbtg179uwR7ztp0iSMHDkSHTp0QKdOnbB06VJkZ2dj1KhR1fRpPKLNUZ1DF1MxaVssHuQUAAAMpRK81cERHZ3rIz45s9rO5jOQSjDb3xVjNkRDAmhMbRbffba/K88JJCIivaXXoao8vv32W0ilUgwcOBB5eXnw8/PD6tWrxesGBgbYvXs3xowZAx8fH5iammLkyJH4/PPPxT7Ozs7Ys2cPJk6ciGXLlqFx48b4/vvvxT2qAGDw4MG4e/cuZs2aheTkZHh6eiI8PLzE4vXqUDyqk6zMLXVdlQSA3TNGdQpUany9Lx7fHb4mtlmZGkMCYNOJm9h04iaA6t0jqo+7PULe9i6xT5Ud96kiIqIaoEbsU1VbaHOfquKn/4DSR3We9vTfrQc5GLs5BjE308W2to0VOHNLWaKvLvaIquq9t4iIiCqiVu1TRSUVj+o8eYCxnUL+1AD057lk9F9+RAxURgYSfNa/DVIzSl9/pYs9ogykEvg0t8Zrno3g09yagYqIiGqEGj/9V5f1cbdHL1e7co3q5Beq8dUfF/Hj0QSxzdHKBCsDvZGTr0JyRl6J1xTjHlFERETPxlBVwxWP6jzNzfs5CN4crTG919fdDl8NbAuFiRF+j71drntxjygiIqKyMVTVcnvPJmHaL2eQmVcIADA2kOKzAW0wvIsTJJKiES3uEUVERPT8GKpqqdwCFb7YcwH/d/yG2NbUuh5WDvWGeyOFRl9tPE1IRERU13Ghei2UcC8bA0OOaQQq/3YOCBvbrUSgAh7tEQWgxOab3COKiIiofBiqapldp+9gwPJ/ce5O0eHNMkMpvnzdA8uHeMJcblTm6yr7NCEREREV4fRfLZFboMLcsPPY/N+mnQDQrKEpVg31Rhv78u2JVZGnCYmIiEgTQ1UtcCU1C8GbonExOVNse8OrEeYFuMNUVrF/xeV5mpCIiIhKYqiq4aJupGH4DyeQk68CAMiNpPj8NXcMat9YfLqPiIiIqh5DVQ3n5qCAY/16iE/JREsbM6wa5o1Wtua6LouIiKjOYaiq4eRGBlg1zBvrjibg0/5tUM+Y/0qJiIh0gb+Ba4EWNmb44nUPXZdBRERUp3FLBSIiIiItYKgiIiIi0gKGKiIiIiItYKgiIiIi0gKGKiIiIiItYKgiIiIi0gKGKiIiIiItYKgiIiIi0gKGKiIiIiItYKgiIiIi0gKGKiIiIiItYKgiIiIi0gKGKiIiIiItMNR1AXWJIAgAgIyMDB1XQkREROVV/Hu7+Pd4WRiqqlFmZiYAwNHRUceVEBERUUVlZmZCoVCUeV0iPCt2kdao1WrcuXMH5ubmkEgkui6nWmRkZMDR0RGJiYmwsLDQdTl1Dj9/3eLnr1v8/HWrNn3+giAgMzMTDg4OkErLXjnFkapqJJVK0bhxY12XoRMWFhY1/n+qmoyfv27x89ctfv66VVs+/6eNUBXjQnUiIiIiLWCoIiIiItIChiqqUjKZDLNnz4ZMJtN1KXUSP3/d4uevW/z8dasufv5cqE5ERESkBRypIiIiItIChioiIiIiLWCoIiIiItIChioiIiIiLWCoIq1bsGABOnbsCHNzc9jY2CAgIADx8fG6LqvO+uqrryCRSDBhwgRdl1Jn3L59G2+//Tasra1hYmICDw8PnDp1Stdl1QkqlQozZ86Es7MzTExM0Lx5c8ybN++ZZ7ZR5Rw+fBj+/v5wcHCARCLBzp07Na4LgoBZs2bB3t4eJiYm8PX1xeXLl3VTbDVgqCKt++effxAUFITjx49j//79KCgoQO/evZGdna3r0uqckydP4rvvvkPbtm11XUqd8eDBA7zwwgswMjLCH3/8gfPnz2PJkiWoX7++rkurExYuXIiQkBCsXLkSFy5cwMKFC7Fo0SKsWLFC16XVStnZ2WjXrh1WrVpV6vVFixZh+fLlCA0NRWRkJExNTeHn54fc3NxqrrR6cEsFqnJ3796FjY0N/vnnH7z44ou6LqfOyMrKgre3N1avXo358+fD09MTS5cu1XVZtd706dNx9OhR/Pvvv7oupU4aMGAAbG1t8cMPP4htAwcOhImJCTZs2KDDymo/iUSC3377DQEBAQCKRqkcHBwwefJkTJkyBQCgVCpha2uL9evXY8iQITqstmpwpIqqnFKpBABYWVnpuJK6JSgoCP3794evr6+uS6lTdu3ahQ4dOmDQoEGwsbGBl5cX1q5dq+uy6oyuXbviwIEDuHTpEgDg9OnTOHLkCPr27avjyuqehIQEJCcna/wZpFAo0LlzZ0REROiwsqrDA5WpSqnVakyYMAEvvPAC3N3ddV1OnbFlyxZER0fj5MmTui6lzrl27RpCQkIwadIk/O9//8PJkycxbtw4GBsbY+TIkbour9abPn06MjIy4OLiAgMDA6hUKnzxxRcYNmyYrkurc5KTkwEAtra2Gu22trbitdqGoYqqVFBQEOLi4nDkyBFdl1JnJCYmYvz48di/fz/kcrmuy6lz1Go1OnTogC+//BIA4OXlhbi4OISGhjJUVYNt27Zh48aN2LRpE9zc3BAbG4sJEybAwcGBnz9VOU7/UZUJDg7G7t27cejQITRu3FjX5dQZUVFRSE1Nhbe3NwwNDWFoaIh//vkHy5cvh6GhIVQqla5LrNXs7e3h6uqq0damTRvcvHlTRxXVLVOnTsX06dMxZMgQeHh4YPjw4Zg4cSIWLFig69LqHDs7OwBASkqKRntKSop4rbZhqCKtEwQBwcHB+O2333Dw4EE4OzvruqQ6pWfPnjh79ixiY2PFrw4dOmDYsGGIjY2FgYGBrkus1V544YUSW4hcunQJTk5OOqqobsnJyYFUqvmrzcDAAGq1WkcV1V3Ozs6ws7PDgQMHxLaMjAxERkbCx8dHh5VVHU7/kdYFBQVh06ZN+P3332Fubi7OnSsUCpiYmOi4utrP3Ny8xPo1U1NTWFtbc11bNZg4cSK6du2KL7/8Em+99RZOnDiBNWvWYM2aNbourU7w9/fHF198gSZNmsDNzQ0xMTH45ptv8O677+q6tFopKysLV65cEb9PSEhAbGwsrKys0KRJE0yYMAHz589Hy5Yt4ezsjJkzZ8LBwUF8QrDWEYi0DECpX+vWrdN1aXVWjx49hPHjx+u6jDojLCxMcHd3F2QymeDi4iKsWbNG1yXVGRkZGcL48eOFJk2aCHK5XGjWrJnw6aefCnl5ebourVY6dOhQqX/ejxw5UhAEQVCr1cLMmTMFW1tbQSaTCT179hTi4+N1W3QV4j5VRERERFrANVVEREREWsBQRURERKQFDFVEREREWsBQRURERKQFDFVEREREWsBQRURERKQFDFVEREREWsBQRURUA7z00kuYMGGCrssgoqdgqCKiKiUIAnx9feHn51fi2urVq2FpaYlbt27poDJNL730EiQSSYmvjz76SNelAQB27NiBefPm6boMInoK7qhORFUuMTERHh4eWLhwIT788EMARWeEeXh4ICQkBMOHD9fq/QoKCmBkZFSh17z00kto1aoVPv/8c432evXqwcLCQpvlVUh+fj6MjY11dn8iKj+OVBFRlXN0dMSyZcswZcoUJCQkQBAEjB49Gr1794aXlxf69u0LMzMz2NraYvjw4bh375742vDwcHTr1g2WlpawtrbGgAEDcPXqVfH69evXIZFIsHXrVvTo0QNyuRwbN27EjRs34O/vj/r168PU1BRubm7Yu3fvU+usV68e7OzsNL6KA9XPP/8MMzMzXL58Wez/8ccfw8XFBTk5OQCApk2bYt68eQgMDISpqSkaNWqEVatWadwjPT0d7733Hho2bAgLCwu88sorOH36tHh9zpw58PT0xPfffw9nZ2fI5XIAJaf/8vLyMGXKFDRq1Aimpqbo3Lkz/v77b/H6+vXrYWlpiX379qFNmzYwMzNDnz59kJSUpFHPjz/+CDc3N8hkMtjb2yM4OLjctRKRJoYqIqoWI0eORM+ePfHuu+9i5cqViIuLw3fffYdXXnkFXl5eOHXqFMLDw5GSkoK33npLfF12djYmTZqEU6dO4cCBA5BKpXj99dehVqs13n/69OkYP348Lly4AD8/PwQFBSEvLw+HDx/G2bNnsXDhQpiZmVW6/hEjRqBfv34YNmwYCgsLsWfPHnz//ffYuHEj6tWrJ/ZbvHgx2rVrh5iYGLGm/fv3i9cHDRqE1NRU/PHHH4iKioK3tzd69uyJtLQ0sc+VK1fw66+/YseOHYiNjS21nuDgYERERGDLli04c+YMBg0ahD59+miEvpycHHz99df4v//7Pxw+fBg3b97ElClTxOshISEICgrCBx98gLNnz2LXrl1o0aJFhWolosfo8jRnIqpbUlJShAYNGghSqVT47bffhHnz5gm9e/fW6JOYmCgAKPMk+7t37woAhLNnzwqCIAgJCQkCAGHp0qUa/Tw8PIQ5c+aUu7YePXoIRkZGgqmpqcbXhg0bxD5paWlC48aNhTFjxgi2trbCF198ofEeTk5OQp8+fTTaBg8eLPTt21cQBEH4999/BQsLCyE3N1ejT/PmzYXvvvtOEARBmD17tmBkZCSkpqaWqG/8+PGCIAjCjRs3BAMDA+H27dsafXr27CnMmDFDEARBWLdunQBAuHLlinh91apVgq2trfi9g4OD8Omnn5b6eZSnViLSZKjbSEdEdYmNjQ0+/PBD7Ny5EwEBAdi4cSMOHTpU6gjS1atX0apVK1y+fBmzZs1CZGQk7t27J45Q3bx5E+7u7mL/Dh06aLx+3LhxGDNmDP7880/4+vpi4MCBaNu27VPrGzZsGD799FONNltbW/Gf69evjx9++AF+fn7o2rUrpk+fXuI9fHx8Sny/dOlSAMDp06eRlZUFa2trjT4PHz7UmNJ0cnJCw4YNy6zz7NmzUKlUaNWqlUZ7Xl6exnvXq1cPzZs3F7+3t7dHamoqACA1NRV37txBz549S71HeWslokcYqoioWhkaGsLQsOiPnqysLPj7+2PhwoUl+tnb2wMA/P394eTkhLVr18LBwQFqtRru7u7Iz8/X6G9qaqrx/XvvvQc/Pz/s2bMHf/75JxYsWIAlS5Zg7NixZdamUCg0pr9Kc/jwYRgYGCApKQnZ2dkwNzcv188NFP289vb2GmufillaWpb5s5T2PgYGBoiKioKBgYHGtccD6pOL9SUSCYT/nk0yMTHRSq1E9AhDFRHpjLe3N3799Vc0bdpUDFqPu3//PuLj47F27Vp0794dAHDkyJFyv7+joyM++ugjfPTRR5gxYwbWrl371FD1LMeOHcPChQsRFhaGadOmITg4GD/99JNGn+PHj5f4vk2bNgCKft7k5GQYGhqiadOmla7Dy8sLKpUKqamp4udSUebm5mjatCkOHDiAl19+ucR1bdVKVJdwoToR6UxQUBDS0tIQGBiIkydP4urVq9i3bx9GjRoFlUqF+vXrw9raGmvWrMGVK1dw8OBBTJo0qVzvPWHCBOzbtw8JCQmIjo7GoUOHxHBTlpycHCQnJ2t8PXjwAACQmZmJ4cOHY9y4cejbty82btyIrVu34pdfftF4j6NHj2LRokW4dOkSVq1ahe3bt2P8+PEAAF9fX/j4+CAgIAB//vknrl+/jmPHjuHTTz/FqVOnyv25tWrVCsOGDcOIESOwY8cOJCQk4MSJE1iwYAH27NlT7veZM2cOlixZguXLl+Py5cuIjo7GihUrtForUV3CUEVEOuPg4ICjR49CpVKhd+/e8PDwwIQJE2BpaQmpVAqpVIotW7YgKioK7u7umDhxIhYvXlyu91apVAgKCkKbNm3Qp08ftGrVCqtXr37qa9auXQt7e3uNr8DAQADA+PHjYWpqii+//BIA4OHhgS+//BIffvghbt++Lb7H5MmTcerUKXh5eWH+/Pn45ptvxI1PJRIJ9u7dixdffBGjRo1Cq1atMGTIENy4cUNj7VZ5rFu3DiNGjMDkyZPRunVrBAQE4OTJk2jSpEm532PkyJFYunQpVq9eDTc3NwwYMEB8elCbtRLVFdz8k4hIS5o2bYoJEybwOBmiOoojVURERERawFBFREREpAWc/iMiIiLSAo5UEREREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWkBQxURERGRFjBUEREREWnB/wMmm5wHV6djHAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "salary = model.predict([[7]])\n",
        "\n",
        "print(\"Predicted Salary:\", salary[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bLu_frMslTFW",
        "outputId": "c189e99b-062c-4761-9836-72934885cc8e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Predicted Salary: 90346.90874069053\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "experience = float(input(\"Enter Years Experience: \"))\n",
        "\n",
        "salary = model.predict([[experience]])\n",
        "\n",
        "print(\"Predicted Salary:\", salary[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qIkWJudSl6Li",
        "outputId": "a2995185-d8f6-4c94-8c82-831109108e1b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Years Experience: 0.5\n",
            "Predicted Salary: 29092.109140989192\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import joblib\n",
        "\n",
        "joblib.dump(model, \"salary_model.pkl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2A79gJP1mD8a",
        "outputId": "f26d499a-f62e-4d5a-85de-f65aec1188b8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['salary_model.pkl']"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "\n",
        "import joblib\n",
        "\n",
        "model = joblib.load(\"salary_model.pkl\")"
      ],
      "metadata": {
        "id": "OVYnaogYnauo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "files.download(\"salary_model.pkl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "ZFJyq6PE5bd7",
        "outputId": "2e0117f8-0fe6-47d5-e9a3-b26ca1f6f6d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_027d794b-fe94-467d-a8ac-4f23bc5052fa\", \"salary_model.pkl\", 817)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "files.download(\"salary_model.ipynb\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "wWpnUkb9InKq",
        "outputId": "f7c57486-b41e-4633-f4fa-c0f8ae6f28c2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_c79e1b3e-27d9-4518-aa67-1c4f81411661\", \"salary_model.ipynb\", 817)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import joblib\n",
        "\n",
        "model = joblib.load(\"salary_model.pkl\")\n",
        "\n",
        "st.title(\"Salary Prediction App\")\n",
        "\n",
        "experience = st.number_input(\n",
        "    \"Enter Years of Experience\",\n",
        "    min_value=0.0\n",
        ")\n",
        "\n",
        "if st.button(\"Predict\"):\n",
        "    salary = model.predict([[experience]])\n",
        "    st.success(f\"Predicted Salary: ₹{salary[0]:,.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 397
        },
        "id": "sByyRSDhApPc",
        "outputId": "b5774611-b903-47a6-ec03-ba541d15074c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_493/3437542406.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"salary_model.pkl\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    }
  ]
}